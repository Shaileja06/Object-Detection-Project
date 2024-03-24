import os
from dataclasses import dataclass

@dataclass
class Data_preprocessing:
    model_yaml_file: str = 'yolov5/models/yolov5s.yaml'
    custom_yaml_file: str = 'artifacts/'

    def __post_init__(self):
        os.makedirs(self.custom_yaml_file, exist_ok=True)

    def reading_nc(self, path):
         # Your code for reading_nc method here
        pass  # Placeholder, replace with your actual code

    def custom_yaml_model(self, number_of_classes):
        # Your code for custom_yaml_model method here
        pass  # Placeholder, replace with your actual code
