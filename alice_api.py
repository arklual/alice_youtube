import requests
import y
import os
import json

def get_response(text, event, tts=None):
        if not tts:
            return {
                'version': event['version'],
                'session': event['session'],
                'response': {
                    'text': text,
                    'end_session': 'false'
                },
            }
        else:
            return {
                'version': event['version'],
                'session': event['session'],
                'response': {
                    'text': text,
                    'tts': tts,
                    'end_session': 'false'
                },
            } 

def get_input(event):
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = event['request']['original_utterance']
        return text
    return False

def upload_audio(audio):
    headers = {
        'Authorization': 'OAuth y0_AgAAAAAphf1rAAT7owAAAADqVVMYWnxBx9TyQQKqnt5KftPx6ygyJCM',
    }

    files = {
        'file': open(audio, 'rb'),
    }

    response = requests.post('https://dialogs.yandex.net/api/v1/skills/46f17381-7ce6-4393-a3cb-d989a6e8d906/sounds', headers=headers, files=files)
    print(response.json())
    return [audio, response.json()['sound']['id']]

async def delete_all_audios():
    headers = {
        'Authorization': 'OAuth y0_AgAAAAAphf1rAAT7owAAAADqVVMYWnxBx9TyQQKqnt5KftPx6ygyJCM',
    }

    response = requests.get('https://dialogs.yandex.net/api/v1/skills/46f17381-7ce6-4393-a3cb-d989a6e8d906/sounds', headers=headers).json()
    for i in response['sounds']:
        requests.delete(
            f'https://dialogs.yandex.net/api/v1/skills/46f17381-7ce6-4393-a3cb-d989a6e8d906/sounds/{i["id"]}',
            headers=headers,
        )

async def youtube_to_alice(search):
        y.get_playlist(search)
        files = os.listdir('output')
        ids = []
        for f in files:
            ids.append(upload_audio(f'output/{f}'))
            os.remove(f'output/{f}')
        ids = list(sorted(ids, key=lambda x: x[0]))
        to_write = [i[1] for i in ids]
        with open('ids.json', 'w', encoding='utf-8') as file:
            json.dump(to_write, file, ensure_ascii=False)