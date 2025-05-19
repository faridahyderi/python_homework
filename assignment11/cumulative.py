import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("../db/lesson.db")

# SQL query to get total price per order
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Load the query results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Method 1: Add cumulative revenue column using apply() (for learning)
def cumulative(row):
    totals_above = df['total_price'][0:row.name + 1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

# Method 2: (Preferred) Use cumsum() for cumulative sum
# df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs. order_id
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', linestyle='-', color='green')
plt.title('Cumulative Revenue by Order ID')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.show()