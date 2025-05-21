import numpy as np
from typing import Tuple

class QLearningThresholdAdjuster:
    def __init__(self, 
                 state_space: int = 100, 
                 action_space: int = 20,
                 learning_rate: float = 0.1,
                 discount_factor: float = 0.9,
                 exploration_rate: float = 0.2):
        """
        增强版Q-Learning阈值调整器
        参数:
            state_space: 状态空间维度
            action_space: 动作空间维度
            learning_rate: 学习率
            discount_factor: 折扣因子
            exploration_rate: 探索率
        """
        self.state_space = state_space
        self.action_space = action_space
        self.q_table = np.zeros((state_space, action_space))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
    
    def get_action(self, state: int) -> int:
        """
        获取动作策略 (ε-greedy)
        """
        if np.random.random() < self.exploration_rate:
            return np.random.randint(self.action_space)
        return np.argmax(self.q_table[state])
    
    def update_threshold(self, state: int, action: int, reward: float, next_state: int) -> float:
        """
        更新Q值表
        参数:
            state: 当前状态
            action: 采取的动作
            reward: 获得的奖励
            next_state: 转移到的状态
        返回:
            更新后的Q值
        """
        current_q = self.q_table[state, action]
        max_next_q = np.max(self.q_table[next_state])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
        self.q_table[state, action] = new_q
        return new_q
    
    def decay_exploration(self, decay_rate: float = 0.99, min_rate: float = 0.01) -> None:
        """
        衰减探索率
        """
        self.exploration_rate = max(min_rate, self.exploration_rate * decay_rate)