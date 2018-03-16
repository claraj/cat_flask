# Get a cat video from YouTube.
# Set the YOUTUBE_API_KEY as an environment variable

# Helpful Google example: https://github.com/youtube/api-samples/blob/master/python/search.py

# Need the video title. Also the video ID for building a URL to embed the video in a home_page
# https://developers.google.com/youtube/player_parameters

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os

DEVELOPER_KEY = os.environ['YOUTUBE_API_KEY']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def cat_video(category):

    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

        search_response = youtube.search().list(
            q='cat,' + category,
            part='id, snippet',
            maxResults=1,
            type='videos',
            safeSearch='strict'
        ).execute()

        first_result = search_response.get('items', [])[0]
        print(first_result)

        title = first_result['snippet']['title']
        video_id = first_result['id']['videoId']

        return { 'title': title, 'video_id': video_id }

    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(cat_vid('cat'));
