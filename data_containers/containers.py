from . import Container


class TrainContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/train.csv"
        self.columns = ['building_id', 'meter', 'timestamp', 'meter_reading']
        self.read_dataset()


class TestContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/test.csv"
        self.columns = ['row_id', 'building_id', 'meter', 'timestamp']
        self.read_dataset()


class WeatherTrainContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/weather_train.csv"
        self.columns = ['site_id', 'timestamp', 'air_temperature', 'cloud_coverage',
                        'dew_temperature', 'precip_depth_1_hr', 'sea_level_pressure',
                        'wind_direction', 'wind_speed']
        self.read_dataset()


class WeatherTestContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/weather_test.csv"
        self.columns = ['site_id', 'timestamp', 'air_temperature', 'cloud_coverage',
                        'dew_temperature', 'precip_depth_1_hr', 'sea_level_pressure',
                        'wind_direction', 'wind_speed']
        self.read_dataset()


class MetaContainer(Container):
    def __init__(self):
        super().__init__()
        self.path_to_dataset = "datasets/building_metadata.csv"
        self.columns = ['site_id', 'building_id', 'primary_use', 'square_feet', 'year_built',
                        'floor_count']
        self.read_dataset()
