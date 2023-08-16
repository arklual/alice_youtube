import alice_api
from typing import Union
from fastapi import FastAPI
import json

app = FastAPI()

@app.post("/")
def handler(event: dict):
    print(event)
    print('------')
    data = alice_api.get_response('Какой запрос?', event)
    print(data)
    return data
    search = alice_api.get_input(event)
    if search:
        yield alice_api.get_response('Подождите минуту', event)
        ids = alice_api.youtube_to_alice(search)
    else:
        return alice_api.get_response('Какой запрос?', event)