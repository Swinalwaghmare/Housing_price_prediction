import os
from src.Constant import *

# data set file path
data_file_path = os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY)

# Data ingestion config
raw_data_file_path = os.path.join(ROOT_DIR,ARTIFACT_DIR,
                                  DATA_INGESTION_ARTIFACT,
                                  RAW_DATA_KEY)

train_data_file_path = os.path.join(ROOT_DIR,ARTIFACT_DIR,
                                    DATA_INGESTION_ARTIFACT,
                                    TRAIN_DATA_KEY)

test_data_file_path = os.path.join(ROOT_DIR,ARTIFACT_DIR,
                                   DATA_INGESTION_ARTIFACT,
                                    TEST_DATA_KEY)