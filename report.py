def generate_report(schema_issues, null_issues, mean_issue, category_issues, timestamp):
    report = [f"Run Time: {timestamp}\n", "Pipeline Check Report\n"]

    if schema_issues[0]:
        report.append(f"Missing columns: {list(schema_issues[0])}")
    if schema_issues[1]:
        report.append(f"Unexpected columns: {list(schema_issues[1])}")

    if null_issues:
        for col, pct in null_issues:
            report.append(f"High nulls in '{col}': {pct*100}%")

    if mean_issue:
        report.append(f"Price mean shifted by {mean_issue*100}%")

    if category_issues:
        for cat, drop in category_issues:
            report.append(f"Category '{cat}' dropped by {drop*100}%")

    if len(report) == 2:
        report.append("No issues found")

    return "\n".join(report)