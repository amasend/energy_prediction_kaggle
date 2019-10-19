from abc import ABC, abstractmethod
import pandas as pd
from typing import List, Any


class Container(ABC):
    def __init__(self):
        self.data: pd.DataFrame = pd.DataFrame(data=[])

    def read_dataset(self, **kwargs: Any) -> None:
        self.data = pd.read_csv(**kwargs)

    def try_one_hot_encoding(self, **kwargs: Any) -> None:
        try:
            new_columns = kwargs['new_columns']
            del kwargs['new_columns']
            self.data = pd.get_dummies(self.data, **kwargs)
            self.data.columns = new_columns
        except KeyError:
            self.data = pd.get_dummies(self.data, **kwargs)

    @abstractmethod
    def clean_dataset(self) -> None:
        pass
