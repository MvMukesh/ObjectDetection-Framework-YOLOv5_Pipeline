import sys
import yaml
import base64
import os.path
from objectDetectionFramework.logger import logging
from objectDetectionFramework.exception import AppException


# function to read yaml file
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e
    

# function to write YAML file (will not use this function here in this project)
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")
    except Exception as e:
        raise AppException(e, sys)


### --- Image Decoding and Encoding ---
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath): #saving image as jpg file
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

