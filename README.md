# 大模型数据标注平台及AI数据飞轮工程系统

## 项目概述
本项目旨在构建一个高效、智能的大模型数据标注平台，通过自动化工具链和AI预标注技术，显著提升数据标注效率和质量。

## 核心功能
1. **自动化标注工具链**
   - 多算法选优器
   - 多人标注可靠性判别器(t≥3标注者置信区间筛选)
   - 基于强化学习(Q-Learning)的动态阈值调整模块
   - Kubernetes容器化编排 + Airflow DAG调度
   - 动态资源调度算法(DRF策略)

2. **PDF版面解析优化**
   - SAM智能拉框补全
   - SORT算法优化长文本跟踪
   - Re-ID特征融合多目标关联

3. **AI预标注训练架构**
   - Few-shot Learning与增量学习融合
   - GPT预标注→人工校准双重校验
   - 闭环训练链路：GPT标注-人工校准-私有模型训练

4. **两阶段分层训练框架**
   - 80%通参量预训练 + 20%领域LoRA微调
   - 思维链标注(CoT)技术
   - 动态Prompt分析历史错误案例

5. **LLM双引擎质检体系**
   - 生成器(GPT-4 Turbo)与评估器(LLaMA3-70B)角色分离
   - 多维度一致性评估(Dice/F1/Cosine)

## 技术指标
- 系统吞吐量：50万标注单元/天
- 数据流转效率提升：40%
- PDF标注人工量降低：70%
- 预标注准确率：97%(+19pp)
- 标注一致性：92%
- 质检效率提升：30%

## 项目结构
```
├── README.md
├── data
│   ├── raw_data
│   ├── processed_data
│   └── models
├── notebooks
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── inference.ipynb
├── src
│   ├── data_processing.py
│   ├── model_training.py
│   ├── inference.py
│   └── utils.py
├── config
│   ├── config.yaml
│   └── model_config.yaml
├── requirements.txt
├── setup.py
├── tests
│   ├── test_data_processing.py
│   ├── test_model_training.py
│   └── test_inference.py
├── .gitignore
├── LICENSE
└── Dockerfile
```
## 安装依赖
```bash
pip install -r requirements.txt
```
## 运行项目
```bash
python main.py
```
## 测试项目
```bash
pytest