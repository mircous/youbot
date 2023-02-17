from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

try:
    # Use the built-in method to create credentials from a client secret file
    creds = Credentials.from_authorized_user_file(
        "ytbot-377518-0fe7e4e97c47.json",
        scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
    )
    """
    client_id='637748250358-pmqvnel449kssu9asg87odjhsjg7phes.apps.googleusercontent.com',
    client_secret='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',
    redirect_uri='https://accounts.google.com/o/oauth2/auth',
    """
    # Create a YouTube API client using the credentials
    youtube = build('youtube', 'v3', credentials=creds)
    # Get the refresh token from the credentials
    refresh_token = creds.refresh_token
    print('Refresh token:', refresh_token)
except HttpError as error:
    print('An error occurred: %s' % error)
