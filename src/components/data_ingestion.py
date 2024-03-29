from roboflow import Roboflow 
from src.logger import logging  
from src.exception import SignException
from dataclasses import dataclass
import os


@dataclass
class DataIngestion:
    folder: str = os.path.abspath('/config/workspace/data')

    def __post_init__(self):
        os.makedirs(self.folder, exist_ok=True)

    def dataset_download(self):
        try:
            rf = Roboflow(api_key="uurrF6aLt1ryWB3sG8xR")
            project = rf.workspace("project-et9mt").project("signlang-q5xad") 
            dataset = project.version(1).download("yolov5", location=self.folder)
            
            # Make sure to return the absolute path to the downloaded data
            dataset_path = os.path.abspath(self.folder)
            
            logging.info(f'Dataset Downloaded Successfully. Path: {dataset_path}')
            return dataset_path

        except Exception as e:
            logging.error(f'Error in dataset_download: {str(e)}')
            raise SignException(f'Dataset download failed: {str(e)}')

if __name__ == '__main__':
    ingestion = DataIngestion()
    dataset_path = ingestion.dataset_download()
    print(f"Dataset path: {dataset_path}")