# from telebot import TeleBot
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Union
#
#
# class Message(BaseModel):
#     telegram_id : Union[int, List]
#     message: str
#
#
# app = FastAPI()
#
# app.get("/")
# async def home():
#     return {"message": "Hello World"}
#
# app.post("/app/v1/message/send")
# async def send_message(send: Message):
#     print(send)

import random
import string

# get random password pf length 8 with letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(8))
print("Random password is:", password)