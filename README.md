# YouTube Data Pipeline

A complete end-to-end data engineering pipeline built with Docker, Airflow, Redis, PostgreSQL, and Streamlit, designed to fetch YouTube video data, process it, store it, and visualize it.

## 🧱 Project Architecture

![image](https://github.com/user-attachments/assets/2c4ee72f-dee5-4de4-bfac-551c02caa04d)

## 📦 Tech Stack

- **Producer/Consumer**: Python
- **Message Queue**: Redis Streams
- **Database**: PostgreSQL
- **Workflow Orchestration**: Apache Airflow
- **Monitoring**: Streamlit
- **Containerization**: Docker Compose



## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/YouTubeDataPipeline.git
cd YouTubeDataPipeline
```
**2. Set Up YouTube API Key**
Create a .env file in the root directory:
```
YOUTUBE_API_KEY=your_api_key_here
CHANNEL_ID=your_channel_id_here
```
To generate a YouTube API key: [Setup YouTube API Without Billing →]([url](https://console.cloud.google.com))

**3. Run the Pipeline**
```
docker-compose up --build
```
**4. Access the Services**
Service	          URL
Airflow UI	      http://localhost:8080
Streamlit Dash	  http://localhost:8501
PostgreSQL	      localhost:5432/yt
Redis	            localhost:6379



## 📂 Project Structure
![image](https://github.com/user-attachments/assets/6794d444-f78b-40e8-ba65-6b06b07b5cdf)



## ⏱️ Airflow DAG
youtube_data_pipeline: Runs every 6 hours.

Executes the producer script using a BashOperator.

Schedule: 0 */6 * * *

Configurable in dags/youtube_dag.py


## 📌 Future Improvements
Add more DAG tasks: consumer trigger, database validation

Add NLP tagging for video titles

Add Grafana for advanced metrics

Export results to S3 or BigQuery

Add deduplication & error handling

## 👨‍💻 Author
Revisha Shareen Vas

Built for educational purposes and hands-on data engineering experience



