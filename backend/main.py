from fastapi import FastAPI, UploadFile, File
from segment_anything import SamPredictor, sam_model_registry
from fastapi.middleware.cors import CORSMiddleware
from algorithms.threshold_adjuster import QLearningThresholdAdjuster
from airflow import settings
from airflow.models import DagBag

app = FastAPI(title="DataAgent Platform")

# 初始化调整器
adjuster = QLearningThresholdAdjuster()

# 在标注流程中使用
state = get_current_state()  # 获取当前状态
action = adjuster.get_action(state)  # 获取调整动作
new_threshold = apply_action(action)  # 应用新阈值
reward = calculate_reward()  # 计算奖励
next_state = get_next_state()  # 获取新状态

# 更新Q表
adjuster.update_threshold(state, action, reward, next_state)

# 定期衰减探索率
adjuster.decay_exploration()

@app.on_event("startup")
async def startup():
    # 初始化Airflow DAG调度器
    init_airflow_dag()
    # 初始化Kubernetes资源调度
    init_kubernetes_scheduler()


def init_airflow_dag():
    dagbag = DagBag(
        dag_folder='workflow/',
        include_examples=False
    )


def init_kubernetes_scheduler():
    from kubernetes import client, config
    
    # 加载kube配置
    config.load_kube_config()
    
    # 创建DRF调度器配置
    api = client.CoreV1Api()
    api.create_namespaced_config_map(
        namespace="default",
        body={
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {
                "name": "drf-config"
            },
            "data": {
                "policy.json": '{"kind":"Policy","apiVersion":"v1","predicates":[{"name":"PodFitsResources"}],"priorities":[{"name":"DRF","weight":1,"argument":{"drfResources":["cpu","memory"]}}]}'
            }
        }
    )


app = FastAPI()

# 初始化SAM模型
sam = sam_model_registry["vit_b"](checkpoint="sam_vit_b_01ec64.pth")
predictor = SamPredictor(sam)

@app.post("/api/sam/predict")
async def predict_masks(file: UploadFile = File(...)):
    import cv2
    import numpy as np
    
    # 读取并预处理图像
    image_bytes = await file.read()
    image_np = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    
    # 使用SAM预测
    predictor.set_image(image)
    masks, _, _ = predictor.predict()
    
    # 转换结果为前端可用的格式
    results = []
    for mask in masks:
        contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        results.append([contour.tolist() for contour in contours])
    
    return {"masks": results}
