"""
# Primeira DAG - Usando instruções em um bloco with

Testando o Airflow
"""

from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow import DAG

with DAG(
    dag_id="primeira_dag_with",
    start_date=datetime(2025, 11, 9),
    schedule="@daily",
    doc_md=__doc__,
):
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="bash", bash_command='echo "hello world"')
    end = EmptyOperator(task_id="end")

(start >> hello >> end)
