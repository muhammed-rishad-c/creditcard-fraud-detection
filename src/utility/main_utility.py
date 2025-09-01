import numpy as np
from src.exception.custom_exception import CustomException
import os,sys

def save_numpy(filepath:str,file:np.array):
    try:
        dirname=os.path.dirname(filepath)
        os.makedirs(dirname,exist_ok=True)
        with open(filepath,'wb') as obj:
            np.save(obj,file)
            
    except Exception as e:
        raise CustomException(e,sys)