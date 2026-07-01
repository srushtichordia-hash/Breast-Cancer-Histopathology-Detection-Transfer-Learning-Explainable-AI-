from pathlib import Path

import cv2
import pandas as pd
import torch
from torch.utils.data import Dataset


class BreakHisDataset(Dataset):

    def __init__(
        self,
        metadata: pd.DataFrame,
        transform=None,
    ):
        self.metadata = metadata.reset_index(drop=True)
        self.transform = transform

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, index):
        pass