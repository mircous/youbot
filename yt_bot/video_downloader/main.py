import requests
import json
from random import randint
from moviepy.editor import *
from search import *

list_of_keywords = []

def id():
    while True:
        try:
            headers = {
                'Authorization': 'YOUR_API_KEY',
            }

            key_list = ["cat", "dog", "dolphin", "monkey", "lion", "zebra", "rat", "mouse", "bird", "tiger", "bird", "pig", "turtle", "elephant", " giraffe", "kangaroo", "wolf", "human", "snake", "bear", "deer"]
            video_index = randint(1, 20)
            search_word = key_list[video_index]
            ran_page = randint(1,5)
            print("adding id of ", search_word, "video!")
            params = {
                'query': search_word,
                'page': ran_page,
                'per_page': '1',
            }

            response = requests.get('https://api.pexels.com/videos/search', params=params, headers=headers)
            id = response.json()["videos"][0]['id']
            list_of_keywords.append(search_word)
            #print(list_of_keywords)
            return str(id)

        except:
            print("there is an erRor!")

headers = {
    'Authorization': 'YOUR_API_KEY',
}

times = int(input("How many videos?"))

lst = []
lst_of_id = []
for x in range(times):
    lst_of_id.append(id())

#print(lst_of_id)

percent = 0
for id in lst_of_id:
    response = requests.get(
        "https://api.pexels.com/videos/videos/"+id,
        headers=headers
    )
    print("Starting Video download.Process on", str(percent)+"%")
    percent += (100/times)
    if response.status_code == 200:
        video_data = json.loads(response.text)
        j_index = 0
        try:
            while True:
                cur_dict = video_data['video_files'][j_index]
                if cur_dict["quality"] == "hd":
                    break
                else:
                    print("searchin for right sized video!")
                    j_index += 1
                    pass
            video_url = video_data['video_files'][j_index]['link']
            response = requests.get(video_url, stream=True)
            if response.status_code == 200:
                lst.append("/home/mircous/Downloads/gitytbot/yt_bot/video_downloader/"+ id+".mp4")
                with open(id+".mp4", "wb") as f:
                    for chunk in response:
                        f.write(chunk)
                print("video dowloaded! +" + str(100/times) + "%")
            else:
                print("Error while downloading the video.")
        except:
            pass
    else:
        print("Error while fetching the video information.")

final = []
num = randint(4,5)
for i in lst:
    #print(lst)
    try:
        final.append(VideoFileClip(i).subclip(num,7))
    except:
        try:
            final.append(VideoFileClip(i).subclip(2,num))
        except:
            final.append(VideoFileClip(i).subclip(1,3))


final_exact = concatenate_videoclips(final)

final_exact.write_videofile("edited_video.mp4")
print(list_of_keywords)
