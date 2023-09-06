import os
from dotenv import load_dotenv

load_dotenv()

model_file = 'yolov8n.pt'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_MODEL = os.path.join(BASE_DIR, 'ml', model_file)
RTSP_URL = 0


DB_NAME = os.environ.get("DB_NAMME")
