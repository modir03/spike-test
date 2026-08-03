from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="spike_test_dag",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    tags=["spike", "test"],
) as dag:
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    start >> end
