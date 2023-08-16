import requests
import y
import os

def get_response(text, event):
        return {
            'version': event['version'],
            'session': event['session'],
            'response': {
                'text': text,
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
    return response.json['id']

def youtube_to_alice(search):
        y.get_playlist(search)
        files = os.listdir('output')
        ids = []
        for f in files:
            ids.append(upload_audio(f'output/{f}'))
        return ids