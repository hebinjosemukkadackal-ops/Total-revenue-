import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to database
conn = sqlite3.connect("D:\ElevateLab_Task7\sales_data.db")

# 2. SQL Query to get total quantity and revenue per product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# 3. Print results
print("Sales Summary:")
print(df)

# 4. Plot bar chart of revenue
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.ylabel("Revenue")
plt.title("Revenue per Product")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save chart
plt.show()

# Close connection
conn.close()
