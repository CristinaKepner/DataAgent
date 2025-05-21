import pytest
from algorithms.threshold_adjuster import QLearningThresholdAdjuster

def test_q_learning_update():
    adjuster = QLearningThresholdAdjuster()
    state = 0
    action = adjuster.get_action(state)
    reward = 1.0
    next_state = 1
    updated_q = adjuster.update_threshold(state, action, reward, next_state)
    assert updated_q > 0