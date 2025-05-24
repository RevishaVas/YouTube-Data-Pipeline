from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='youtube_data_pipeline',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='0 */6 * * *',  # every 6 hours
    catchup=False,
    tags=['youtube', 'data'],
) as dag:

    run_producer = BashOperator(
        task_id='run_producer_script',
        bash_command='python /opt/airflow/producer/producer.py'
    )

    run_producer
