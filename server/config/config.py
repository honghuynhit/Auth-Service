import os

from pydantic import BaseSettings
from pymongo import MongoClient


# class Settings(BaseSettings):
#     app_name: str = "Awesome API"
#     admin_email: str
#     items_per_user: int = 50

#     class Config:
#         env_file = ".env"

class Config:
    port = os.getenv('SERVICE_PORT', 2000)
    address = os.getenv('SERVICE_ADDRESS' or 'auth_service')
    registry_host = os.getenv('REGISTRY_HOST' or 'registry')
    registry_port = os.getenv('REGISTRY_PORT' or 2000)

    # Get DB host from docker-compose environment
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = "auth_service"
    REMOTE_MONGO_URL = "mongodb+srv://biaclem:mongobiaclem.online@biaclem.8m5h1jk.mongodb.net/test"

    if REMOTE_MONGO_URL:
        MONGO_CLIENT = MongoClient(REMOTE_MONGO_URL)
    elif all([DB_HOST, DB_PORT]):
        MONGO_CLIENT = MongoClient(f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?authMechanism=SCRAM-SHA-256')
