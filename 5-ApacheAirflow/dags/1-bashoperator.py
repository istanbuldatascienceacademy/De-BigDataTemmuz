from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum # alternatif olarak datetime modülü de kullanılabilir


dag = DAG(
    dag_id="1-bashoperator",
    start_date=pendulum.datetime(2024,3,28), # year, month, day, hour, minute, second, microsecond
    schedule_interval="@daily", # her gün çalıştır , @hourly, @weekly, @monthly, @yearly
    catchup=False # aradaki kaçırılan işlemleri çalıştırma
)

# BashOperator ile bir bash komutu çalıştırabiliriz
# task_id : görevin adı
# bash_command : çalıştırılacak bash komutu
# dag : hangi dag içinde çalıştırılacağı

t1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag
)

t2 = BashOperator(
    task_id="print_hello",
    bash_command="echo hello",
    dag=dag
)

t3 = BashOperator(
    task_id="print_world",
    bash_command="echo world",
    dag=dag
)

t1 >> t2 >> t3