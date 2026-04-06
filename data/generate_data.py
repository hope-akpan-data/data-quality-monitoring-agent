import pandas as pd

# previous (good data)
prev = pd.DataFrame({
    "product_id": [1,2,3,4],
    "price": [100, 200, 300, 400],
    "category": ["electronics", "electronics", "home", "home"]
})

# current (broken data)
curr = pd.DataFrame({
    "id": [1,2,3,4],
    "price": [100, None, None, None],
    "category": ["electronics", "electronics", "electronics", "electronics"]
})

prev.to_parquet("data/previous.parquet")
curr.to_parquet("data/current.parquet")

print("Sample data created")