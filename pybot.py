import requests

url = "https://api.telegram.org/bot1062798887:AAHGlmS2tJDkOiag3boqZ4re8Fo2zFblhX8/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
