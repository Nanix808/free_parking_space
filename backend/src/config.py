import os
from dotenv import load_dotenv

load_dotenv()

model_file='yolov8n.pt'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_MODEL = os.path.join(BASE_DIR, 'ml', model_file)
# RTSP_URL = 'rtsp://root:Password01@172.16.10.245:554/live.sdp'
# RTSP_URL = 'rtsp://admin:Password01@172.16.10.18:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
RTSP_URL = 0





# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(BASEDIR, '.env'))


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAMME")
