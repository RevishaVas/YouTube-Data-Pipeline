from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'revisha',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='youtube_fetch_pipeline',
    default_args=default_args,
    description='Fetch YouTube videos every 15 minutes',
    schedule_interval='*/15 * * * *',
    start_date=datetime(2025, 5, 25),
    catchup=False,
) as dag:
    fetch_task = BashOperator(
        task_id='fetch_youtube',
        bash_command='python /opt/airflow/producer/fetch_youtube.py'
    )
