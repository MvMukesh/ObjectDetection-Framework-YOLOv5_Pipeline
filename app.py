import sys
from objectDetectionFramework.logger import logging
from objectDetectionFramework.exception import AppException 

try:
    a = 777 / "mukeshmanral"

except Exception as e:
    raise AppException(e,sys)