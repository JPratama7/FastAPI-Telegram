from pydantic import BaseModel
from typing import List, Union
from fastapi import FastAPI, HTTPException
from telebot import TeleBot
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TELE = getenv("API")
TOKEN = getenv("TOKEN")


class Message(BaseModel):
    token: str
    telegram_id : Union[int, List]
    message: str

bot = TeleBot(TELE)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/app/v1/message/send")
async def send_message(send: Message):
    telegram_id = send.telegram_id
    message = send.message
    if send.token == TOKEN:
        if isinstance(telegram_id, list):
            for i in telegram_id:
                try:
                    bot.send_message(i, message)
                except:
                    print("Error", i)
        else:
            try:
                bot.send_message(telegram_id, message)
            except:
                raise HTTPException(status_code=400, detail="Telegram ID is not valid")

        return {"message": "Message sent"}
    else:
        raise HTTPException(status_code=400, detail="Token is not valid")