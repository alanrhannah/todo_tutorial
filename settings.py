import os 

BASE_DIR = os.environ['TODO_DIR']
JSON_FILE = os.environ['TODO_JSON_FILE']
DATA_DIR = 'data'
DATA_PATH = os.path.join(BASE_DIR, DATA_DIR)

if not os.path.exists(DATA_PATH):
	os.makedirs(DATA_PATH)

JSON_PATH = os.path.join(DATA_PATH, JSON_FILE)
