import logging
from datetime import datetime
import os

ROOT_FILE_PATH = 'F:\Ineuron\Project\gemstone_price_prediction'
log_dir = 'logs'
current_time_stamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

log_file = f'log_{current_time_stamp}.log'
logs_path = os.path.join(ROOT_FILE_PATH,log_dir)

os.makedirs(logs_path,exist_ok=True)

log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path, 
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)