# Task 1
import sqlite3
import os

def create_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to database at {db_path}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    db_dir = "../db"
    db_file = "magazines.db"
    db_path = os.path.join(db_dir, db_file)

    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    create_connection(db_path)

#Task 2

if __name__ == "__main__":
    db_dir = "../db"
    db_file = "magazines.db"
    db_path = os.path.join(db_dir, db_file)

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        );
        """)

        conn.commit()
        print("Tables created successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if conn:
            conn.close()

#Task 3            
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.Error as e:
        print(f"Error inserting publisher {name}: {e}")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.Error as e:
        print(f"Error inserting magazine {name}: {e}")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("""
            INSERT INTO subscribers (name, address)
            SELECT ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM subscribers WHERE name = ? AND address = ?
            )
        """, (name, address, name, address))
    except sqlite3.Error as e:
        print(f"Error inserting subscriber {name}: {e}")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                       (subscriber_id, magazine_id, expiration_date))
    except sqlite3.Error as e:
        print(f"Error inserting subscription: {e}")

if __name__ == "__main__":
    db_dir = "../db"
    db_file = "magazines.db"
    db_path = os.path.join(db_dir, db_file)

    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key checking
        cursor = conn.cursor()

        add_publisher(cursor, "TechMedia")
        add_publisher(cursor, "HealthPress")
        add_publisher(cursor, "Foodies Inc")

        add_magazine(cursor, "India Today", 1)
        add_magazine(cursor, "Healthy Living", 2)
        add_magazine(cursor, "Grocery Monthly", 3)

        add_subscriber(cursor, "Alice Smith", "123 Main St")
        add_subscriber(cursor, "Bob Johnson", "456 Oak Ave")
        add_subscriber(cursor, "Carol Davis", "789 Pine Rd")

        add_subscription(cursor, 1, 1, "2025-04-30")
        add_subscription(cursor, 2, 2, "2025-06-15")
        add_subscription(cursor, 3, 3, "2025-09-01")

        conn.commit()
        print("Tables created and populated successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if conn:
            conn.close()


#Task 4
if __name__ == "__main__":
    db_dir = "../db"
    db_file = "magazines.db"
    db_path = os.path.join(db_dir, db_file)

    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key checking
        cursor = conn.cursor()   

        print("\nAll Subscribers:")
        cursor.execute("SELECT * FROM subscribers;")
        subscribers = cursor.fetchall()
        for sub in subscribers:
            print(sub)   

        print("\nAll Magazines Sorted by Name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name;")
        magazines = cursor.fetchall()
        for mag in magazines:
            print(mag)         

        print("\nMagazines Published by TechMedia:")
        cursor.execute("""
            SELECT magazines.*
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.id
            WHERE publishers.name = 'TechMedia';
        """)
        techmedia_magazines = cursor.fetchall()
        for mag in techmedia_magazines:
            print(mag)         

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if conn:
            conn.close()
        
#Task 5        