from decouple import config
from urllib.parse import quote
from pymongo import MongoClient

class Database:
    DB_NAME: str = config("DB_NAME")
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = quote(config("DB_PASSWORD"))
    DB_SERVER: str = config("DB_SERVER")
    DB_PORT: str = config("DB_PORT")

    # MongoDB connection string format if the db has authorization enabled
    #DATABASE_URL = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}?authSource=admin"
    DATABASE_URL = f"mongodb://{DB_SERVER}:{DB_PORT}/"

database = Database()

client = MongoClient(database.DATABASE_URL)
db = client[database.DB_NAME]