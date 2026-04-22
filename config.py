import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temple-secret-key-12345'
    # 使用全新的 SQLite V2 讓 Schema 生效
    SQLALCHEMY_DATABASE_URI = 'sqlite:///temple_v3.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
