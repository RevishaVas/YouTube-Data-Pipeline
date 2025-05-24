import redis
import psycopg2
import time # Importing necessary libraries

r = redis.Redis(host='redis', port=6379, decode_responses=True)
conn = psycopg2.connect(host="postgres", dbname="yt", user="postgres", password="pass")
cur = conn.cursor()

def consume():
    last_id = '0-0'
    while True:
        try:
            msg = r.xread({'youtube_stream': last_id}, block=0, count=1)
            if msg:
                _, data = msg[0]
                for message_id, values in data:
                    last_id = message_id
                    cur.execute("""
                        INSERT INTO videos (video_id, title, channel, published_at)
                        VALUES (%s, %s, %s, %s)
                    """, (
                        values['video_id'],
                        values['title'],
                        values['channel'],
                        values['published_at']
                    ))
                    conn.commit()
                    print(f"✅ Inserted video: {values['title']}")
        except Exception as e:
            print("❌ Error:", e)
            time.sleep(2)

if __name__ == "__main__":
    consume()
