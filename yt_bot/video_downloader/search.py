import requests
from random import randint


def id():
    headers = {
        'Authorization': 'YOUR_API_KEY',
    }

    key_list = ["cat", "dog", "dolphin", "monkey", "lion", "zebra", "rat", "mouse", "bird", "tiger", "bird", "pig", "turtle", "elephant", " giraffe", "kangaroo", "wolf", "human", "snake", "bear", "deer"]
    video_index = randint(1, 20)
    search_word = key_list[video_index]

    params = {
        'query': search_word,
        'page': video_index,
        'per_page': '1',
    }

    response = requests.get('https://api.pexels.com/videos/search', params=params, headers=headers)
    id = response.json()["videos"][0]['id']
    return str(id)
