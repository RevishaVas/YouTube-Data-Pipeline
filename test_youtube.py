from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

response = youtube.search().list(
    q="data engineering",
    part="snippet",
    type="video",
    maxResults=5
).execute()

for item in response['items']:
    print(f"📹 {item['snippet']['title']} | 📺 {item['snippet']['channelTitle']}")
