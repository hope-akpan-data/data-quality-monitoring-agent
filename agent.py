import pandas as pd
from checks import *
from report import generate_report
from datetime import datetime

# Load data
curr = pd.read_parquet("data/current.parquet")
prev = pd.read_parquet("data/previous.parquet")

# Run checks
schema_issues = check_schema(curr, "config/schema.json")
null_issues = check_nulls(curr)
mean_issue = check_mean_shift(curr, prev, "price")
category_issues = check_category_drop(curr, prev, "category")

# Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Generate report
report = generate_report(schema_issues, null_issues, mean_issue, category_issues, timestamp)

# Save report to file
with open("report.txt", "w") as f:
    f.write(report)

# Print report & simulate alert
print(report)
print("\nALERT SENT TO DATA TEAM")