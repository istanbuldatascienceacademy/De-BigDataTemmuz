from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pendulum
import requests


def isim_don():
    return "Yusuf"

# ti : task instance airflow içindeki tasklar arasında veri paylaşımı yapmamızı sağlar
# xcom_pull ile veriyi çekebiliriz
def isim_birlestir(soyad,ti):
    ad = ti.xcom_pull("ilk_task")
    print(f"ikinci fonksiyon çalıştı. Merhaba {ad} {soyad}")



# xcom_push ile veri paylaşımı yapabiliriz
# xcom_pull ile veriyi çekebiliriz
def set_title_completed(ti):
    req = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = req.json()
    title = data["title"]
    completed = data["completed"]
    ti.xcom_push(key="title", value=title)
    ti.xcom_push(key="completed", value=completed)


def get_title_completed(ti):
    title = ti.xcom_pull(key="title", task_ids="set_title_completed")
    completed = ti.xcom_pull(key="completed", task_ids="set_title_completed")
    print(f"title: {title}, completed: {completed}")

dag = DAG(
    dag_id="2-pythonoperator2",
    start_date=pendulum.datetime(2024,3,28), # year, month, day, hour, minute, second, microsecond
    schedule_interval="@daily", # her gün çalıştır , @hourly, @weekly, @monthly, @yearly
    catchup=False # aradaki kaçırılan işlemleri çalıştırma
)

t1 = PythonOperator(
    task_id="ilk_task",
    python_callable=isim_don,
    dag=dag
)

t2 = PythonOperator(
    task_id="ikinci_task",
    python_callable=isim_birlestir,
    op_kwargs={"soyad":"GZB"},
    dag=dag
)

t3 = PythonOperator(
    task_id="set_title_completed",
    python_callable=set_title_completed,
    dag=dag
)

t4 = PythonOperator(
    task_id="get_title_completed",
    python_callable=get_title_completed,
    dag=dag
)

t1 >> t2 >> t3 >> t4