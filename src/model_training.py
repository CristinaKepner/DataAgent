from peft import LoraConfig, get_peft_model
import torch
from transformers import AutoModelForSequenceClassification

class TwoPhaseTrainer:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        
    def pretrain(self, train_data):
        # 加载基础模型
        model = AutoModelForSequenceClassification.from_pretrained(
            self.config["training"]["base_model"])
        
        # 80%参数预训练
        for name, param in model.named_parameters():
            if "classifier" not in name:  # 排除分类层
                param.requires_grad = True
        
        # ... 预训练逻辑 ...
    
    def lora_finetune(self, model, domain_data):
        # 配置LoRA
        lora_config = LoraConfig(
            r=self.config["training"]["lora"]["r"],
            lora_alpha=self.config["training"]["lora"]["alpha"],
            target_modules=["query", "value"],
            lora_dropout=self.config["training"]["lora"]["dropout"],
            bias="none"
        )
        
        # 应用LoRA
        model = get_peft_model(model, lora_config)
        # ... 微调逻辑 ...