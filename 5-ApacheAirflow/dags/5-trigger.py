from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum

dag = DAG(
    dag_id='5-trigger',
    start_date=pendulum.datetime(2023, 12, 13),
    schedule_interval='@daily',# @hourly, @weekly, @monthly, @yearly , cron expression
    catchup=False # false olursa aradaki boşlukları çalıştırmaz
    )


# Trigger Rolleri
# all_success -> tüm tasklar başarılı olursa çalışır
# all_failed -> tüm tasklar başarısız olursa çalışır
# all_done -> tüm tasklar çalışırsa çalışır
# one_success -> bir task başarılı olursa çalışır
# one_failed -> bir task başarısız olursa çalışır
# none_failed -> hiç task başarısız olmazsa çalışır
# none_skipped -> hiç task skip olmazsa çalışır
# none_failed_or_skipped -> hiç task başarısız veya skip olmazsa çalışır


ilk_task = BashOperator(
    task_id='ilk_task',
    bash_command='echo "ilk task çalıştı"',
    dag=dag
    )

ikinci_task = BashOperator(
    task_id='ikinci_task',
    bash_command='python deneme.py', # hata verecek 
    dag=dag
    )

ucuncu_task = BashOperator(
    task_id='ucuncu_task',
    bash_command='pwd',
    trigger_rule='one_failed',# bir task başarısız olursa çalışır eğer task başarılı olursa çalışmaz  
    dag=dag
    )

task4 = BashOperator(
    task_id='task4',
    bash_command='sleep 10',
    trigger_rule='none_failed',# hiçbir task başarısız olmazsa çalışır
    dag=dag
    )


task5 = BashOperator(
    task_id='task5',
    bash_command='echo "task5 çalıştı"',
    trigger_rule='all_success',# tüm tasklar başarılı olursa çalışır
    dag=dag
    )

ilk_task >> ikinci_task >> ucuncu_task >> task4 >>  task5
