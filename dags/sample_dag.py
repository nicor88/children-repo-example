"""
Sample Airflow DAG with 3 tasks.

This DAG includes:
- Start task (DummyOperator)
- Process task (PythonOperator)
- End task (DummyOperator)
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'sample_dag',
    default_args=default_args,
    description='A sample Airflow DAG for demonstration',
    schedule_interval=timedelta(days=1),  # Run daily
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['sample', 'example'],
) as dag:

    # Task 1: Start task
    start_task = DummyOperator(
        task_id='start',
    )

    # Task 2: Process data
    def process_data(**context):
        """Sample Python function to process data."""
        print(f"Processing data for execution date: {context['ds']}")
        # Simulate some processing
        data = [1, 2, 3, 4, 5]
        result = sum(data)
        print(f"Processed data result: {result}")
        return result

    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )

    # Task 3: End task
    end_task = DummyOperator(
        task_id='end',
    )

    # Define task dependencies
    start_task >> process_task >> end_task

