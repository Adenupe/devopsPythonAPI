#import os
from fastapi import FastAPI
from app.api.routes import tasks
from app.core import config
#from dotenv import load_dotenv


#load_dotenv()

#app_name = os.getenv("APP_NAME")
#mongo_url = os.getenv("MONGO_URL")
#print(mongo_url)

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def home():
    return {"status":"app is live"}

@app.get("/health")
def health():
    return {"status":"Healthy"}

@app.get("/info")
def info():
    return {"name of application is: ": config.app_name}
