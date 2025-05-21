import torch
from torch.utils.data import Dataset

class IncrementalDataset(Dataset):
    def __init__(self, base_data, new_data):
        self.data = base_data + new_data
        
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __len__(self):
        return len(self.data)