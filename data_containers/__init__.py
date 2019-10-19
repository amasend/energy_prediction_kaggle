from abc import ABC
import pandas as pd
from typing import List


class Container(ABC):
    def __init__(self):
        self.path_to_dataset: str = ''
        self.columns: List[str] = []
        self.data: pd.DataFrame = pd.DataFrame(data=[])

    def read_dataset(self):
        self.data = pd.read_csv(filepath_or_buffer=self.path_to_dataset,
                                header=0,
                                names=self.columns)
