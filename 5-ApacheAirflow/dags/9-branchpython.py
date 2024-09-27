from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator # Hiçbir işlem yapmayan bir operatör
import pendulum
import requests

def kara_ver_fonk():
    url_lik = "http://api.weatherapi.com/v1/current.json"
    access_key = "fe661b56017447dab3d24625220704"

    il = "Istanbul"

    response = requests.get(url=url_lik,params={"key":access_key,"q": f"{il}"}).json()

    deger = {
        "il": response["location"]["name"],
        "sıcaklık": response["current"]["temp_c"],
    }

    if deger["sıcaklık"] >= 20:
        return "sicak_task"
    elif deger["sıcaklık"] >15 and deger["sıcaklık"] < 20:
        return "ılık_task"
    else:
        return "soguk_task"

dag = DAG(
    dag_id='9-branchpython',
    start_date=pendulum.datetime(2023, 10, 13),
    schedule_interval='@daily',# @hourly, @weekly, @monthly, @yearly , cron expression
    catchup=False
    )

kara_ver = BranchPythonOperator(
    task_id='kara_ver',
    python_callable=kara_ver_fonk,
    dag=dag
    )

sicak_task = DummyOperator(task_id='sicak_task', dag=dag)
ılık_task = DummyOperator(task_id='ılık_task', dag=dag)
soguk_task = DummyOperator(task_id='soguk_task', dag=dag)
son_task = DummyOperator(task_id='son_task', trigger_rule='none_failed', dag=dag)


kara_ver >> [sicak_task,ılık_task,soguk_task] >> son_task