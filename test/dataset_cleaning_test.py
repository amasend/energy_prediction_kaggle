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

    # !!!!!!!!!! #
    #    Load    #
    # !!!!!!!!!! #
    def test_00_01_check_if_train_dataset_loaded_correctly(self) -> None:
        size_of_loaded_dataset = self.train_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.train_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.train_data.columns)

        print("First 5 elements of loaded dataset:")
        print(self.train_data.data.head())

    @unittest.SkipTest
    def test_00_02_check_if_test_dataset_loaded_correctly(self) -> None:
        size_of_loaded_dataset = self.test_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.test_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.test_data.columns)

        print("First 5 elements of loaded dataset:")
        print(self.test_data.data.head())

    @unittest.SkipTest
    def test_00_03_check_if_weather_train_dataset_loaded_correctly(self) -> None:
        size_of_loaded_dataset = self.weather_train_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.weather_train_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.weather_train_data.columns)

        print("First 5 elements of loaded dataset:")
        print(self.weather_train_data.data.head())

    @unittest.SkipTest
    def test_00_04_check_if_weather_test_dataset_loaded_correctly(self) -> None:
        size_of_loaded_dataset = self.weather_test_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.weather_test_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.weather_test_data.columns)

        print("First 5 elements of loaded dataset:")
        print(self.weather_test_data.data.head())

    @unittest.SkipTest
    def test_00_05_check_if_meta_dataset_loaded_correctly(self) -> None:
        size_of_loaded_dataset = self.meta_data.data.size
        self.assertGreater(size_of_loaded_dataset, 0)

        columns = self.meta_data.data.columns.to_list()
        self.custom_assert.assert_columns_equal(columns, self.meta_data.columns)

        print("First 5 elements of loaded dataset:")
        print(self.meta_data.data.head())

    # !!!!!!!!!! #
    #  Prepare   #
    # !!!!!!!!!! #
    def test_01_01_check_one_hot_encoding_train_dataset(self) -> None:
        print("Training dataset columns before one hot encoding:")
        print(self.train_data.columns)
        new_columns = ['building_id', 'meter_reading', 'meter_electricity',
                       'meter_chilledwater', 'meter_steam', 'meter_hotwater']
        self.train_data.try_one_hot_encoding(columns=['meter'],
                                             new_columns=new_columns)
        self.assertGreater(len(self.train_data.data.columns),
                           len(self.train_data.columns))
        print("Training dataset columns after one hot encoding:")
        print(self.train_data.data.columns)
