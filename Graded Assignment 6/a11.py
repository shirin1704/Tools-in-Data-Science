import sqlite3
import math

# Connect to (or create) an SQLite database
conn = sqlite3.connect('correlation_analysis.db')  # or ':memory:' for in-memory

# Read the SQL file
with open('q-sql-correlation.sql', 'r') as f:
    sql_script = f.read()

# Execute the entire SQL script
cursor = conn.cursor()
#cursor.executescript(sql_script)

# Optional: Fetch data from a table to verify
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

cursor.execute("""
SELECT
    COUNT(*) as n,
    SUM(study_hours_per_week) as sum_x,
    SUM(completion_rate) as sum_y,
    SUM(study_hours_per_week * completion_rate) as sum_xy,
    SUM(study_hours_per_week * study_hours_per_week) as sum_x2,
    SUM(completion_rate * completion_rate) as sum_y2
FROM student_learning_data;
""")

# Fetch values
n, sum_x, sum_y, sum_xy, sum_x2, sum_y2 = cursor.fetchone()

# Compute Pearson r
numerator = n * sum_xy - sum_x * sum_y
denominator = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

r = numerator / denominator if denominator != 0 else None

print("Pearson correlation coefficient:", r)

# Always close the connection
conn.close()
