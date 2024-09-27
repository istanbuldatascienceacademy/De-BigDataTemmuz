from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sql import BranchSQLOperator # true false -- 0 - 1 

import pendulum


create_table_sql = '''
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INTEGER
        );
    '''

insert_data_sql = '''
    INSERT INTO my_table (name, age) VALUES ('ahmet', 25), ('mehmet', 30), ('mustafa', 40);
'''

dag = DAG(
    dag_id="9-brenchSql",
    schedule="@daily",
    start_date=pendulum.datetime(2023,9,24,tz="UTC"),
    catchup=False
    ) 

create_table_task = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='baglanti_postgre',
    sql=create_table_sql,
    dag=dag)

insert_data_task = PostgresOperator(
    task_id='insert_data',
    postgres_conn_id='baglanti_postgre',
    sql=insert_data_sql,
    dag=dag)

check_data_task = BranchSQLOperator(
    task_id='check_data',
    conn_id='baglanti_postgre',
    # sql="select age from my_table where age > 600;",

    # my_table tablosunda age kolonu 30'dan büyük olan bir veri var mı yok mu kontrol et
    # varsa 1 yoksa 0 döndür
    sql="""
            SELECT 
                CASE 
                    WHEN EXISTS 
                            (SELECT 1 FROM my_table WHERE age > 30) THEN 1 
                    ELSE 0 
                END;
        """,

    # 1 dönerse data_true_task'e git, 0 dönerse data_false_task'e git
    follow_task_ids_if_true='data_true_task',
    follow_task_ids_if_false='data_false_task',
    dag=dag
    )

data_true_task = DummyOperator(task_id='data_true_task', dag=dag)
data_false_task = DummyOperator(task_id='data_false_task', dag=dag)

son_task = DummyOperator(task_id='son_task', trigger_rule='none_failed', dag=dag)

create_table_task >> insert_data_task >> check_data_task >> [data_true_task, data_false_task] >> son_task

