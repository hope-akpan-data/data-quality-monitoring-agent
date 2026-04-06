import json

def check_schema(df, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)

    expected_cols = set(schema["columns"])
    actual_cols = set(df.columns)

    missing = expected_cols - actual_cols
    extra = actual_cols - expected_cols

    return missing, extra

def check_nulls(df, threshold=0.3):
    issues = []

    for col in df.columns:
        null_pct = df[col].isnull().mean()
        if null_pct > threshold:
            issues.append((col, round(null_pct, 2)))

    return issues

def check_mean_shift(curr_df, prev_df, col, threshold=0.5):
    if col not in curr_df or col not in prev_df:
        return None

    curr_mean = curr_df[col].mean()
    prev_mean = prev_df[col].mean()

    if prev_mean == 0:
        return None

    change = abs(curr_mean - prev_mean) / prev_mean

    if change > threshold:
        return round(change, 2)

    return None

def check_category_drop(curr_df, prev_df, col, threshold=0.5):
    if col not in curr_df or col not in prev_df:
        return []

    curr_counts = curr_df[col].value_counts(normalize=True)
    prev_counts = prev_df[col].value_counts(normalize=True)

    issues = []

    for category in prev_counts.index:
        curr_val = curr_counts.get(category, 0)
        prev_val = prev_counts[category]

        if prev_val > 0:
            drop = (prev_val - curr_val) / prev_val
            if drop > threshold:
                issues.append((category, round(drop, 2)))

    return issues