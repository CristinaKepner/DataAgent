from fastapi import FastAPI
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
