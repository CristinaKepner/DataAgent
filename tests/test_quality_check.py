import pytest
from src.quality_check import DualEngineQualityCheck

def test_cross_validation():
    checker = DualEngineQualityCheck()
    test_data = {"text": "sample", "labels": ["A", "B"]}
    result = checker.cross_validate(test_data)
    assert 0 <= result["dice_score"] <= 1
    assert 0 <= result["f1_score"] <= 1