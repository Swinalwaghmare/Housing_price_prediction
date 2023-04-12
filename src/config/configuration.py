import os
from src.Constant import *

# data set file path
data_file_path = os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY)

# Data ingestion config
raw_data_file_path = os.path.join(ROOT_DIR,ARTIFACT_DIR,
                                  DATA_INGESTION_ARTIFACT,
                                  INGESTED_RAW_DIR,INGESTED_RAW_DIR_KEY)

train_data_file_path = os.path.join(ROOT_DIR,ARTIFACT_DIR,DATA_INGESTION_ARTIFACT,
                                    INGESTED_TRAIN_TEST_DIR,TRAIN_DATA_KEY)

test_data_file_path = os.path.join(ROOT_DIR,ARTIFACT_DIR,DATA_INGESTION_ARTIFACT,
                                    INGESTED_TRAIN_TEST_DIR,TEST_DATA_KEY)