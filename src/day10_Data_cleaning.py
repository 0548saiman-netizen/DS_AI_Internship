# Task 1

import pandas as pd

data = {
    "order_id": [1001, 1002, 1003, None, 1005, 1006, 1007, 1008, 1002, 1009, 1010, 1006, None],
    "customer_id": ["C001","C002","C003","C004","C005","C006","C007","C008","C002","C009","C010","C006","C011"],
    "order_date": [
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08","2024-01-09",
        "2024-01-10","2024-01-11","2024-01-12","2024-01-06","2024-01-13",
        "2024-01-14","2024-01-10","2024-01-15"
    ],
    "product": [
        "Laptop","Phone","Tablet","Monitor","Keyboard",
        "Mouse","Headphones","Printer","Phone","Desk",
        "Chair","Mouse","Webcam"
    ],
    "quantity": [1,2,1,2,None,3,1,1,2,1,2,3,1],
    "price": [1200,800,600,300,50,25,None,200,800,350,150,25,100],
    "total_amount": [1200,1600,600,600,None,75,150,200,1600,350,300,75,100]
}

df = pd.DataFrame(data)

print("Initial DataFrame shape:", df.shape)

print("\nMissing values per column:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

df_cleaned = df.drop_duplicates()

print("\nDataFrame shape after cleaning:", df_cleaned.shape)
print("\nCleaned DataFrame preview:")
print(df_cleaned)

# Task 2

import pandas as pd

data = {
    "order_id": [1001, 1002, 1003, 1004],
    "product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "price": ["$1200", "$800", "$600", "$300"],  
    "order_date": ["2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08"]  
}

df = pd.DataFrame(data)

print("Initial data types:")
print(df.dtypes)

df['price'] = df['price'].str.replace('$', '', regex=True).astype(float)

df['order_date'] = pd.to_datetime(df['order_date'])

print("\nData types after conversion:")
print(df.dtypes)

print("\nCleaned DataFrame:")
print(df)

# Task 3

import pandas as pd

data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles "]
}

df = pd.DataFrame(data)

print("Original unique locations:")
print(df['location'].unique())

df['location'] = df['location'].str.strip().str.title()  # Remove whitespace + title case

print("\nNormalized unique locations:")
print(df['location'].unique())

print("\nCleaned DataFrame:")
print(df)






