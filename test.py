import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'meta': {
        'locale': 'ru-RU',
        'timezone': 'UTC',
        'client_id': 'ru.yandex.searchplugin/7.16 (none none; android 4.4.2)',
        'interfaces': {
            'screen': {},
            'payments': {},
            'account_linking': {},
        },
    },
    'session': {
        'message_id': 0,
        'session_id': '430bfbbb-ee99-4067-a9ac-f62bfb195343',
        'skill_id': '46f17381-7ce6-4393-a3cb-d989a6e8d906',
        'user': {
            'user_id': 'CF6D6D8CDB0B94B597721543E75494323B8503E5661087414FB12CB45138FA6D',
        },
        'application': {
            'application_id': '0D7B242C184E36BCBE6C6009A9739EA14547FCFE6031A550C83603E990DEC8D5',
        },
        'user_id': '0D7B242C184E36BCBE6C6009A9739EA14547FCFE6031A550C83603E990DEC8D5',
        'new': True,
    },
    'request': {
        'command': '',
        'original_utterance': '',
        'nlu': {
            'tokens': [],
            'entities': [],
            'intents': {},
        },
        'markup': {
            'dangerous_context': False,
        },
        'type': 'SimpleUtterance',
    },
    'state': {
        'session': {},
        'user': {},
        'application': {},
    },
    'version': '1.0',
}

response = requests.post('http://localhost:8001/skill/', headers=headers, json=json_data)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n  "meta": {\n    "locale": "ru-RU",\n    "timezone": "UTC",\n    "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",\n    "interfaces": {\n      "screen": {},\n      "payments": {},\n      "account_linking": {}\n    }\n  },\n  "session": {\n    "message_id": 0,\n    "session_id": "430bfbbb-ee99-4067-a9ac-f62bfb195343",\n    "skill_id": "46f17381-7ce6-4393-a3cb-d989a6e8d906",\n    "user": {\n      "user_id": "CF6D6D8CDB0B94B597721543E75494323B8503E5661087414FB12CB45138FA6D"\n    },\n    "application": {\n      "application_id": "0D7B242C184E36BCBE6C6009A9739EA14547FCFE6031A550C83603E990DEC8D5"\n    },\n    "user_id": "0D7B242C184E36BCBE6C6009A9739EA14547FCFE6031A550C83603E990DEC8D5",\n    "new": true\n  },\n  "request": {\n    "command": "",\n    "original_utterance": "",\n    "nlu": {\n      "tokens": [],\n      "entities": [],\n      "intents": {}\n    },\n    "markup": {\n      "dangerous_context": false\n    },\n    "type": "SimpleUtterance"\n  },\n  "state": {\n    "session": {},\n    "user": {},\n    "application": {}\n  },\n  "version": "1.0"\n}'
#response = requests.post('https://kind-snowflake-02213.pktriot.net/skill/', headers=headers, data=data)