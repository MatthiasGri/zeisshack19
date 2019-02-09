import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

data_folder = r"C:\Users\mosegui\Desktop\ZEISS Hackathon\zeisshack19\data"  # use your own path
train_file = os.path.join(data_folder, r"c99temp_train_pseudo.snappy.parquet")
valid_file = os.path.join(data_folder, r"c99temp_valid_pseudo.snappy.parquet")

def read_in_data(datafile):
    """
    """
    data = pd.read_parquet(datafile)
    data.index = [data.cpuType, data.cpuBoard, data.timestamp]
    data = data[['tempBoardAK0', 'tempBoardSLAVE', 'remainingLifetime', 'machineNumberPseudo']]
    logger.info(f'data {datafile} read in')

    return data

if __name__ == "__main__":
    data = read_in_data(train_file)  #multi-index df