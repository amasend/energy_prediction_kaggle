from . import Container
import numpy as np


class TrainContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/train.csv"
        self.columns = ['building_id', 'meter', 'meter_reading']
        self.read_dataset(filepath_or_buffer=self.path_to_dataset,
                          header=0,
                          dtype={'building_id': np.int32,
                                 'meter': np.int32,
                                 'timestamp': str,
                                 'meter_reading': np.float32},
                          parse_dates=['timestamp'],
                          index_col=2)

    def clean_dataset(self):
        pass


class TestContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/test.csv"
        self.columns = ['row_id', 'building_id', 'meter']
        self.read_dataset(filepath_or_buffer=self.path_to_dataset,
                          parse_dates=['timestamp'],
                          index_col=3)

    def clean_dataset(self):
        pass


class WeatherTrainContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/weather_train.csv"
        self.columns = ['site_id', 'timestamp', 'air_temperature', 'cloud_coverage',
                        'dew_temperature', 'precip_depth_1_hr', 'sea_level_pressure',
                        'wind_direction', 'wind_speed']
        self.read_dataset(filepath_or_buffer=self.path_to_dataset)

    def clean_dataset(self):
        pass


class WeatherTestContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/weather_test.csv"
        self.columns = ['site_id', 'timestamp', 'air_temperature', 'cloud_coverage',
                        'dew_temperature', 'precip_depth_1_hr', 'sea_level_pressure',
                        'wind_direction', 'wind_speed']
        self.read_dataset(filepath_or_buffer=self.path_to_dataset)

    def clean_dataset(self):
        pass


class MetaContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/building_metadata.csv"
        self.columns = ['site_id', 'building_id', 'primary_use', 'square_feet', 'year_built',
                        'floor_count']
        self.read_dataset(filepath_or_buffer=self.path_to_dataset,
                          dtype={
                              'site_id': np.int32,
                              'building_id': np.int32,
                              'primary_use': str,
                              'square_feet': np.float64,
                          },
                          header=0)

    def clean_dataset(self):
        pass
