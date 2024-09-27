from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum
from datetime import datetime

dag = DAG(
    dag_id='3-retry',
    start_date=pendulum.datetime(2023, 12, 13),
    schedule_interval='@daily',# @hourly, @weekly, @monthly, @yearly , cron expression
    catchup=False # false olursa aradaki boşlukları çalıştırmaz
    )

ilk_task = BashOperator(
    task_id='ilk_task',
    bash_command='python deneme.py',
    retries=3, # kaç kere tekrar deneyecek
    retry_delay=pendulum.duration(seconds=30), # datetime.timedelta(seconds=30), # pendulum.duration(seconds=30)
    dag=dag
    )


ilk_task 