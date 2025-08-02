import sqlite3
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect('regression_analysis.db')

with open('q-sql-regression.sql', 'r') as f:
    sql_script = f.read()

cursor = conn.cursor()
#cursor.executescript(sql_script)

#cursor.execute("SELECT * from delivery_data")
#print(cursor.fetchall())

cursor.execute("SELECT delivery_time_minutes as minutes FROM delivery_data")

minutes = cursor.fetchall()

minutes = [minute[0] for minute in minutes]

cursor.execute("SELECT distance_km as distance FROM delivery_data")

distance = cursor.fetchall()

distance = [dist[0] for dist in distance]

#print(minutes)
#print(distance)

regressor = LinearRegression()

import numpy as np

minutes = np.array(minutes)
distance = np.array(distance).reshape(-1, 1)

regressor.fit(distance, minutes)
print(regressor.coef_)
print(regressor.intercept_)

conn.close()