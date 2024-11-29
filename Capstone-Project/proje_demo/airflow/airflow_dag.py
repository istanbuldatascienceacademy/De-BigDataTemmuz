from airflow import DAG
import pendulum
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryCreateEmptyTableOperator,
    BigQueryDeleteDatasetOperator,
    BigQueryDeleteTableOperator,
    BigQueryGetDatasetTablesOperator,
    BigQueryUpdateDatasetOperator,
    BigQueryUpdateTableOperator,
    BigQueryUpdateTableSchemaOperator,
    BigQueryUpsertTableOperator,
)




PROJE_AD = "qwiklabs-gcp-01-57ba1841032c"
DB_AD = "istdsa"

dag =  DAG(
    dag_id="18_GCSToBigQuery",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC"),
    catchup=False,
    )

sorgu =f"SELECT * FROM `data-to-insights.ecommerce.products` LIMIT 1000"

create_new_table = BigQueryExecuteQueryOperator(
        task_id = "create_new_table",
        sql=sorgu,
        destination_dataset_table=f"{PROJE_AD}.{DB_AD}.butun_veri_analiz_proje",
        create_disposition="CREATE_IF_NEEDED", 
        write_disposition="WRITE_TRUNCATE",#  WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
        use_legacy_sql=False,
        gcp_conn_id="google_cloud_default",
        dag=dag
    )
create_new_table
