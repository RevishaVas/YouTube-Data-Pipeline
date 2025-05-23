CREATE TABLE IF NOT EXISTS videos (
    id SERIAL PRIMARY KEY,
    video_id TEXT,
    title TEXT,
    channel TEXT,
    published_at TIMESTAMP
);
