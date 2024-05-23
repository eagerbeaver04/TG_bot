import schedule
from fastapi import FastAPI
import datetime
from main import bot

app = FastAPI()


@app.post('/notify')
async def notify():
    schedule.run_pending()