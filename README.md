# Memecoin Data Platform

Production-inspired cloud-native data engineering project for ingesting and processing memecoin market data using Azure and PySpark.

---

## Tech Stack

- Python
- CoinGecko API
- Azure Blob Storage
- Azure Data Factory
- Azure Databricks
- PySpark
- Delta Lake
- Azure SQL

---

## Project Architecture

CoinGecko API
↓
Python Ingestion
↓
Azure Blob Storage (Bronze)
↓
Azure Data Factory
↓
Azure Databricks + PySpark
↓
Delta Lake (Silver/Gold)
↓
Azure SQL Analytics

---

## Features

- Automated memecoin market data ingestion
- Raw data storage in Bronze layer
- Data cleaning and transformation using PySpark
- Medallion architecture implementation
- Delta Lake storage format
- Cloud-native Azure data pipeline
- SQL analytics layer

---

## Current Progress

- [x] CoinGecko API ingestion
- [x] Raw CSV generation
- [x] GitHub repository setup
- [ ] Azure Blob Storage integration
- [ ] Azure Data Factory pipeline
- [ ] Databricks transformations
- [ ] Delta Lake implementation
- [ ] Azure SQL integration

---

## Project Structure

```text
memecoin-data-platform/
│
├── architecture/
├── configs/
├── data/
├── ingestion/
├── notebooks/
├── pipelines/
├── sql/
├── logs/
├── tests/
├── requirements.txt
└── README.md
```
