from pathlib import Path

import pandas as pd


class BreakHisParser:

    def __init__(self, dataset_path: Path):
        self.dataset_path = dataset_path

    def build_metadata(self) -> pd.DataFrame:
        pass