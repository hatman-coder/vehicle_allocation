from fastapi import FastAPI
from core.settings import db

def db_connection():
    try:
        db.list_collection_names()
        print("\n------------ Database connected ------------\n")
    except Exception as e:
        print(f"Failed to connect to database: {e}")

def start_application():
    app = FastAPI()
    db_connection()
    return app

app = start_application()
