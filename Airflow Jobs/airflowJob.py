from datetime import timedelta
from airflow import DAG
from airflow.opertors.python_opertor import PythonOperator
from datetime import datetime

def f1():
        print("hello")


with DAG(
    dag_id:"sample",
    schedule_interval:"@daily",
    default_args={
    "owner":"airflow",
    "retry":1,
    "retry_delay":timedelta(minutes=5),
    "start_date":datetime(23,2,15)
    },
    catchup=False
    ) as f:
    f1 = PythonOperator(
            task_id='f1',
            python_callback=f1
        )








        


