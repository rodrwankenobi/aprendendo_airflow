"""
# Primeira DAG - Usando DAG como variável

Testando o Airflow
"""

from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow import DAG

minha_dag = DAG(
    dag_id="primeira_dag_variavel",
    start_date=datetime(2025, 11, 9),
    schedule="@daily",
    doc_md=__doc__,
)
start = EmptyOperator(task_id="start", dag = minha_dag)
hello = BashOperator(task_id="bash", bash_command='echo "hello world"', dag = minha_dag)
end = EmptyOperator(task_id="end", dag = minha_dag)

(start >> hello >> end)
