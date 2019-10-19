import unittest
from data_containers.containers import TrainContainer, TestContainer, WeatherContainer, MetaContainer


class CleanData(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        """Read datasets (train, test, metadata, weather)."""
        cls.train_data = TrainContainer()
        cls.test_data = TestContainer()
        cls.weather_data = WeatherContainer()
        cls.meta_data = MetaContainer()
