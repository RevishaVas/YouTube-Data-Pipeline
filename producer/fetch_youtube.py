import redis
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Redis setup
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# YouTube API setup
youtube = build("youtube", "v3", developerKey=API_KEY)

def fetch_videos():
    response = youtube.search().list(
        q="data engineering",
        part="snippet",
        type="video",
        maxResults=5
    ).execute()

    for item in response['items']:
        data = {
            "video_id": item['id']['videoId'],
            "title": item['snippet']['title'],
            "channel": item['snippet']['channelTitle'],
            "published_at": item['snippet']['publishedAt']
        }
        r.xadd("youtube_stream", data)
        print(f"✅ Pushed video: {data['title']}")

if __name__ == "__main__":
    fetch_videos()
