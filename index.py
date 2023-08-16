from pydantic import BaseModel
import alice_api
from typing import Union
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
import json
import asyncio
from typing import Dict
from data import r, result, ids

app = FastAPI()

@app.post("/skill/")
async def handler(request: Request):
    global r, result, ids
    event = await request.json()
    print(event)
    print('------')
    data = alice_api.get_response('Какой запрос?', event)
    print(data)
    search = alice_api.get_input(event)
    if search and not r:
        asyncio.create_task(alice_api.youtube_to_alice(search))
        r = True
        return alice_api.get_response('Подождите минуту', event)
    elif search and r and 'далее' not in search:
        with open('ids.json', 'r') as f:
            ids = json.load(f)
        if ids == []:
            return alice_api.get_response('Ещё гружу', event)
        mmsg = ''
        for id in ids:
            mmsg += f"<speaker audio='dialogs-upload/46f17381-7ce6-4393-a3cb-d989a6e8d906/{id}.opus'>"
        return alice_api.get_response('Начинаю воспроизведение', event, tts=mmsg)   
    elif search and r and 'далее' in search:
        num = int(search.split(' ')[1].replace('один', '1').replace('два', '2').replace('три', '3').replace('четыре', '4').replace('пять', '5').replace('шесть', '6').replace('семь', '7').replace('восемь', '8').replace('девять', '9'))-1
        with open('ids.json', 'r') as f:
            ids = json.load(f)
        if ids == []:
            return alice_api.get_response('Ещё гружу', event)
        return alice_api.get_response('Начинаю воспроизведение', event, tts=f"<speaker audio='dialogs-upload/46f17381-7ce6-4393-a3cb-d989a6e8d906/{ids[num]}.opus'>")  
    else:
        return alice_api.get_response('Какой запрос?', event)