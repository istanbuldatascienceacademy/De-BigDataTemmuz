from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum

dag = DAG(
    dag_id='4-multpledep',
    start_date=pendulum.datetime(2024, 7, 13),
    schedule_interval='@daily',# @hourly, @weekly, @monthly, @yearly , cron expression
    catchup=False # false olursa aradaki boşlukları çalıştırmaz
    )


ilk_task = BashOperator(
    task_id='ilk_task',
    bash_command='echo "ilk task çalıştı"',
    dag=dag
    )

ikinci_task = BashOperator(
    task_id='ikinci_task',
    bash_command='echo "ikinci task çalıştı"',
    dag=dag
    )

ucuncu_task = BashOperator(
    task_id='ucuncu_task',
    bash_command='pwd',
    dag=dag
    )

task4 = BashOperator(
    task_id='task4',
    bash_command='sleep 30',
    dag=dag
    )

task5 = BashOperator(
    task_id='task5',
    bash_command='echo "task5 çalıştı"',
    dag=dag
    )

ilk_task >> [ikinci_task, ucuncu_task, task4] >> task5