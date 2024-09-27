from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
import pendulum

PROJECT_ID = "first-server-434406-f6"
DATASET="ecommerce"


dag = DAG(
    dag_id="12-GCS_to_BQ",
    start_date=pendulum.datetime(2023, 12, 6),
    schedule_interval="@daily", # @once, @hourly, @daily, @weekly, @monthly
    catchup=False
)

# upload_to_gcs = LocalFilesystemToGCSOperator(
#     task_id="upload_to_gcs",
#     bucket="de_nisan",
#     src="/opt/airflow/dags/data/employees.csv",
#     dst="employees.csv",
#     gcp_conn_id="google_cloud_default",
#     dag=dag
# )


gcs_to_bq = GCSToBigQueryOperator(
    task_id="gcs_to_bq",
    bucket="istdsa123",
    source_objects="employees.csv", # ["Employee1.csv", "Employee2.csv"], ["*.csv"],  "*.json", ["*"]
    source_format="CSV", # CSV, PARQUET, ORC, AVRO, NEWLINE_DELIMITED_JSON
    field_delimiter=",", # "," for CSV, "\t" for TSV, "|" for PSV
    destination_project_dataset_table=f"{PROJECT_ID}.{DATASET}.employees",
    schema_fields=None, # [{"name": "id", "type": "INTEGER", "mode": "REQUIRED"}, {"name": "name", "type": "STRING", "mode": "NULLABLE"}]
    
    # CREATE_IF_NEEDED: tablo yoksa oluşturur
    # CREATE_NEVER: tablo yoksa hata verir
    create_disposition="CREATE_IF_NEEDED", 
    
    # WRITE_TRUNCATE: tablo varsa içindekileri siler ve yazar
    # WRITE_APPEND: tablo varsa devamına yazar
    # WRITE_EMPTY: tablo varsa hata verir, yoksa yazar
    write_disposition="WRITE_APPEND", # WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
    gcp_conn_id="google_cloud_default",
    dag=dag
)


sorgu =f"Select * from {PROJECT_ID}.{DATASET}.employees WHERE salary > 7000"

bq_sorgu = BigQueryExecuteQueryOperator(
    task_id="bq_sorgu",
    sql=sorgu,
    use_legacy_sql=False,
    # destination_dataset_table=None, # Projede tablo oluşturmak istiyorsak buraya yazılır
    destination_dataset_table=f"{PROJECT_ID}.{DATASET}.employee1", # employee1 adında tablo oluşturur
    write_disposition="WRITE_TRUNCATE",
    create_disposition="CREATE_IF_NEEDED",
    gcp_conn_id="google_cloud_default",
    dag=dag
)

# upload_to_gcs >> gcs_to_bq >> bq_sorgu

gcs_to_bq >> bq_sorgu
