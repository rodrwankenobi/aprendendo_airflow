"""
# Primeira DAG - Usando Decorator

Testando o Airflow
"""

from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.decorators import dag

@dag(
    dag_id="primeira_dag_decorator",
    start_date=datetime(2025, 11, 9),
    schedule="@daily",
    doc_md=__doc__,
)
def create_dag():
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="bash", bash_command='echo "hello world"')
    end = EmptyOperator(task_id="end")
    (start >> hello >> end)

criar_dag = create_dag()