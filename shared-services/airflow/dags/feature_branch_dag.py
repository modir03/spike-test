from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def feature_task():
    print("This DAG was created on a feature branch in SMUS and merged to dev")
    return "deployed via branch workflow"


with DAG(
    dag_id="feature_branch_dag",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
    tags=["spike", "feature-branch-test"],
) as dag:
    task = PythonOperator(
        task_id="feature_task",
        python_callable=feature_task,
    )
