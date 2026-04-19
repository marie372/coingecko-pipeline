#!/bin/bash
set -e

echo "Waiting for airflow-db to be ready..."
until pg_isready -h airflow-db -U airflow; do
  sleep 2
done

echo "Installing requirements..."
pip install -r /requirements.txt

echo "Initializing Airflow database..."
airflow db init

echo "Creating admin user..."
airflow users create \
  --username admin \
  --password admin \
  --firstname Marie \
  --lastname Dev \
  --role Admin \
  --email marie@example.com || true

echo "Starting Airflow..."
airflow webserver & airflow scheduler