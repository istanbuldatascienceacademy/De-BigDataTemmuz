from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import pendulum

dag = DAG(
    dag_id='8-SQLExecuteQueryOperator',
    start_date=pendulum.datetime(2023, 10, 13),
    schedule_interval='@daily',  # @hourly, @weekly, @monthly, @yearly , cron expression
    catchup=False
)

create_table = SQLExecuteQueryOperator(
    task_id='create_table',
    conn_id='baglanti_postgre',
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
insert_table = SQLExecuteQueryOperator(
    task_id='insert_table',
    conn_id='baglanti_postgre',
    sql="""
        INSERT INTO dag_runs (tarih, dag_id) VALUES ('{{ ds }}', '{{ dag.dag_id }}')
            """,
    dag=dag
    )

create_table >> insert_table