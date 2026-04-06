# Data Quality Monitoring Agent

A lightweight data validation tool that detects silent failures in data pipelines.

## Problem
Data pipelines often succeed while producing incorrect data (schema changes, null spikes, distribution shifts).

## Solution
This agent runs after pipeline execution and flags:
- Schema mismatches
- High null values
- Data distribution changes

## Example Output;
Pipeline Check Report

Missing columns: ['product_id']
Unexpected columns: ['id']
High nulls in 'price': 75.0%
Category 'home' dropped by 100.0%


## Tech Stack
- Python
- Pandas

## Use Case
Designed for data teams to catch issues before they affect dashboards or models.
