import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

PROFILES_DB = os.path.join(DATA_DIR, 'profiles.pickle')
DB_HANDLER = 'utils.db.PickledDB'
