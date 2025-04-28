import sqlite3
import pandas as pd

# Step 1: Connect to the database
conn = sqlite3.connect('../db/lesson.db')

# Step 2: Write the SQL query to join line_items and products
query = '''
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM 
    line_items
JOIN 
    products
ON 
    line_items.product_id = products.product_id
'''

# Step 3: Load the query results into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Print the first 5 rows to verify
print("Initial DataFrame:")
print(df.head())

# Step 5: Add a 'total' column (quantity * price)
df['total'] = df['quantity'] * df['price']

# Step 6: Print again to verify
print("\nDataFrame with 'total' column:")
print(df.head())

# Step 7: Group by product_id
grouped = df.groupby('product_id').agg(
    line_item_count=('line_item_id', 'count'),
    total_price=('total', 'sum'),
    product_name=('product_name', 'first')
).reset_index()

# Step 8: Sort by product_name
grouped = grouped.sort_values('product_name')

# Step 9: Print the first 5 lines of the grouped DataFrame
print("\nGrouped and Sorted DataFrame:")
print(grouped.head())

# Step 10: Save the result to order_summary.csv
grouped.to_csv('order_summary.csv', index=False)

# Close the connection
conn.close()