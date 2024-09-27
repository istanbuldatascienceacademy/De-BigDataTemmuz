from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pendulum

dag = DAG(
    dag_id='7-postgreoperator',
    start_date=pendulum.datetime(2023, 10, 13),
    schedule_interval='@daily',# @hourly, @weekly, @monthly, @yearly , cron expression
    catchup=False # aradaki kaçırılan işlemleri çalıştırma
    )

create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='baglanti_postgre',
    sql="""
        CREATE TABLE IF NOT EXISTS dag_runs (
            id SERIAL PRIMARY KEY,
            tarih DATE,
            dag_id VARCHAR(50)
        )
            """,   
    dag=dag
    )
# https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
insert_table = PostgresOperator(
    task_id='insert_table',
    postgres_conn_id='baglanti_postgre',
    sql="""
        INSERT INTO dag_runs (tarih, dag_id) VALUES ('{{ ds }}', '{{ dag.dag_id }}')
            """,
    dag=dag
    )

create_table >> insert_table