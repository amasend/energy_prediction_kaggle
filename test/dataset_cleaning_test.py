import unittest
from data_containers.containers import TrainContainer, TestContainer, WeatherTestContainer, WeatherTrainContainer, \
    MetaContainer
from test_utils.asserts import CustomAssert


class CleanData(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        """Read datasets (train, test, metadata, weather)."""
        cls.train_data = TrainContainer()
        cls.test_data = TestContainer()
        cls.weather_train_data = WeatherTrainContainer()
        cls.weather_test_data = WeatherTestContainer()
        cls.meta_data = MetaContainer()
        cls.custom_assert = CustomAssert()

    def test_01_check_if_train_dataset_loaded_correctly(self):
        size_of_loaded_dataset = self.train_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.train_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.train_data.columns)

    def test_02_check_if_test_dataset_loaded_correctly(self):
        size_of_loaded_dataset = self.test_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.test_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.test_data.columns)

    def test_03_check_if_weather_train_dataset_loaded_correctly(self):
        size_of_loaded_dataset = self.weather_train_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.weather_train_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.weather_train_data.columns)

    def test_04_check_if_weather_test_dataset_loaded_correctly(self):
        size_of_loaded_dataset = self.weather_test_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.weather_test_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.weather_test_data.columns)

    def test_05_check_if_meta_dataset_loaded_correctly(self):
        size_of_loaded_dataset = self.meta_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.meta_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.meta_data.columns)
