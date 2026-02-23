import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create the sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample sales data
sample_data = [
    ("Product A", 10, 20.5),
    ("Product B", 5, 15.0),
    ("Product A", 7, 20.5),
    ("Product C", 3, 25.0),
    ("Product B", 8, 15.0),
    ("Product C", 4, 25.0),
    ("Product D", 12, 30.0)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database 'sales_data.db' created successfully with sample data.")
