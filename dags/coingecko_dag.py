from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.insert(0, "/opt/airflow/src")

from extract import fetch_crypto_data
from transform import transform_crypto_data
from load import load_crypto_data

default_args = {
    "owner": "marie",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="coingecko_pipeline",
    default_args=default_args,
    description="Fetch crypto prices from CoinGecko every hour",
    schedule_interval="@hourly",
    start_date=datetime(2026, 4, 19),
    catchup=False,
) as dag:

    def run_pipeline():
        raw = fetch_crypto_data()
        df = transform_crypto_data(raw)
        load_crypto_data(df)

    pipeline_task = PythonOperator(
        task_id="run_coingecko_pipeline",
        python_callable=run_pipeline,
    )