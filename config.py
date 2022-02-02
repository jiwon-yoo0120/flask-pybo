import os

BASE_DIR = os.path.dirname(__file__) # 현재 파일 디렉터리 경로 

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# pybo.db라는 데이터베이스 파일을 프로젝트의 루트 디렉터리에 저장하려는 작업

SECRET_KEY = "dev"