import csv
import os
import django
import sys

# 현재 디렉토리 경로 표시
os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

# 프로젝트명.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalpjt.settings")
django.setup()

from movies.models import OTT

# csv 파일 경로
CSV_PATH = 'ott.csv'	

# encoding 설정 필요
with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)