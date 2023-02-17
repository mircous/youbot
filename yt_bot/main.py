import requests
import json
from search import id


headers = {
    'Authorization': 'YOUR_API_KEY',
}



#response = requests.get('https://api.pexels.com/videos/search', params=params, headers=headers)
#print(response.json())
response = requests.get(
    "https://api.pexels.com/videos/videos/"+id(),
    headers=headers
)


if response.status_code == 200:
    video_data = json.loads(response.text)
    video_url = video_data['video_files'][0]['link']

    response = requests.get(video_url, stream=True)

    if response.status_code == 200:
        with open(id()+".mp4", "wb") as f:
            for chunk in response:
                f.write(chunk)
    else:
        print("Error while downloading the video.")
else:
    print("Error while fetching the video information.")

#video_req.iter_content(chunk_size = 1920*1080):
#    if chunk:
