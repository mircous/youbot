import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account


# Replace with the path to your service account key file
key_file_location = 'client_secret.json'

# Replace with the name of your video file
video_file_path = 'edited_video.mp4'

# Replace with the title of your video
video_title = 'My Video Title'

# Replace with the description of your video
video_description = 'My Video Description'

# Replace with the YouTube video category ID
video_category_id = 22

# Replace with the privacy status of your video
# (options are 'private', 'unlisted', or 'public')
video_privacy_status = 'private'

# Build the credentials object from the service account key file
creds = service_account.Credentials.from_service_account_file(
    key_file_location,
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
)

# Build the YouTube API client
youtube = build('youtube', 'v3', credentials=creds)

# Create a MediaFileUpload object for the video file
video = MediaFileUpload(video_file_path, chunksize=1024*1024, resumable=True)

# Build the request body for the video upload
body = {
    'snippet': {
        'title': video_title,
        'description': video_description,
        'categoryId': video_category_id
    },
    'status': {
        'privacyStatus': video_privacy_status
    }
}

# Send the video upload request
try:
    request = youtube.videos().insert(
        part='snippet, status',
        body=body,
        media_body=video
    )
    response = request.execute()
    print(f'Video uploaded successfully: https://www.youtube.com/watch?v={response["id"]}')
except HttpError as error:
    print(f'An error occurred while uploading the video: {error}')
