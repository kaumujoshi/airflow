from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.docker_operator import DockerOperator

from datetime import datetime

with DAG(
    dag_id='first_sample_dag',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None
) as dag:
    
    read_csv_to_table = DockerOperator(
        task_id='read_csv_to_table',
        image='example_6-backend:latest',
        command="python3 /app/main.py", 
        network_mode='bridge')

read_csv_to_table