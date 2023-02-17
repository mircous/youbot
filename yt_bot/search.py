import requests

def id():
    headers = {
        'Authorization': 'YOUR_API_KEY',
    }

    video_index = "2"
    search_word = "cat"

    params = {
        'query': search_word,
        'page': video_index,
        'per_page': '1',
    }

    response = requests.get('https://api.pexels.com/videos/search', params=params, headers=headers)
    id = response.json()["videos"][0]['id']
    return str(id)
