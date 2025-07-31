import os
from dotenv import load_dotenv

load_dotenv()

HDD_DATA_PATH = os.getenv('hdd_data_path')
KAGGLE_PATH = HDD_DATA_PATH + "/kaggle_data"
CONTEST_PATH = KAGGLE_PATH + "/neurips-open-polymer-prediction-2025"
SUPPLEMENT_PATH = CONTEST_PATH + "/train_supplement"
TEST_CSV = CONTEST_PATH + '/test.csv'
TRAIN_CSV = CONTEST_PATH + '/train.csv'
SAMPLE_SUBMISSION_CSV = CONTEST_PATH + '/sample_submission.csv'