from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pendulum

def print_date():
    print(pendulum.now())

def isim_soyisim_yazdır(ad, soyad):
    print(f"{ad} {soyad}")

dag = DAG(
    dag_id="2-pythonoperator1",
    start_date=pendulum.datetime(2024,3,28), # year, month, day, hour, minute, second, microsecond
    schedule_interval="@daily", # her gün çalıştır , @hourly, @weekly, @monthly, @yearly
    catchup=False # aradaki kaçırılan işlemleri çalıştırma
)

t1 = PythonOperator(
    task_id="print_date",
    python_callable=print_date,
    dag=dag
)

# parametre göndermek için op_args ve op_kwargs kullanılır
t2 = PythonOperator(
    task_id="print_name",
    python_callable=isim_soyisim_yazdır,
    op_kwargs={"ad":"Ahmet", "soyad":"Yılmaz"},
    dag=dag
)

t3 = BashOperator(
    task_id="print_hello",
    bash_command="echo hello",
    dag=dag
)

t1 >> t2 >> t3


