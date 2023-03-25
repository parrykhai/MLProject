import sys
import logging
from exception import CustomException

if __name__=="__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("You are trying to divide by Zero")
        raise CustomException(e, sys)