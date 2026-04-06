# Data Quality Monitoring Agent

A lightweight data validation tool that detects silent failures in data pipelines.

## Problem
Data pipelines often succeed while producing incorrect data (schema changes, null spikes, distribution shifts).

## Solution
This agent runs after pipeline execution and flags:
- Schema mismatches
- High null values
- Data distribution changes

## Example Output;Pipeline Check Report
