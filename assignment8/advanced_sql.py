#Task 1
import sqlite3

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT 
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    print(f"Order ID: {row[0]}, Total Price: ${row[1]}")

conn.close()

#Task 2

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query2 = """
SELECT 
    c.customer_name AS customer_name,
    AVG(sub.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
) AS sub
ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query2)
rows = cursor.fetchall()

for row in rows:
    print(f"Customer: {row[0]}, Average Total Price: ${row[1]}" if row[1] else f"Customer: {row[0]}, No orders")

conn.close()    

#Task 3
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

try:
    # Get customer_id for 'Perez and Sons'
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]
    # Get employee_id for 'Miranda Harris'
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]
    # Get product_ids for 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Insert new order and get the order_id
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, DATE('now'))
        RETURNING order_id
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Insert line items for the order
    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, 10)
        """, (order_id, product_id))

    # Commit the transaction
    conn.commit()

    # Display the inserted line items
    cursor.execute("""
        SELECT l.line_item_id, l.quantity, p.product_name
        FROM line_items l
        JOIN products p ON l.product_id = p.product_id
        WHERE l.order_id = ?
    """, (order_id,))

    rows = cursor.fetchall()
    print("Order created with the following line items:")
    for row in rows:
        print(f"Line Item ID: {row[0]}, Quantity: {row[1]}, Product Name: {row[2]}")

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)

finally:
    conn.close()

#Task 4
try:
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")

    cursor.execute("""
        SELECT 
            e.employee_id,
            e.first_name,
            e.last_name,
            COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
    """)

    rows = cursor.fetchall()
    print("Employees with more than 5 orders:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Orders: {row[3]}")

except Exception as e:
    print("Error:", e)

finally:
    conn.close()    