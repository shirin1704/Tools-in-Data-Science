# employee_viz.py
# Author: 23f2003577@ds.study.iitm.ac.in
# Loads employee data, counts HR frequency, and creates a histogram of departments.
# If 'employees.csv' is present in the working directory, it will be used.
# Otherwise, we fall back to an embedded sample and synthesize up to 100 rows
# to demonstrate the workflow.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import os

def load_employee_data():
    csv_path = "employees.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        return df

    # Fallback to embedded sample (first 5 rows provided)
    sample = (
        "employee_id,department,region,performance_score,years_experience,satisfaction_rating\n"
        "EMP001,Marketing,Middle East,68.82,7,4.7\n"
        "EMP002,Marketing,North America,90.74,8,3.7\n"
        "EMP003,HR,Middle East,80.64,4,3\n"
        "EMP004,Marketing,Europe,70.21,1,3.4\n"
        "EMP005,Sales,Africa,77.31,7,3.5\n"
    )
    df = pd.read_csv(StringIO(sample))

    # Synthesize additional rows to reach 100 entries with realistic distributions
    np.random.seed(42)
    departments = ["HR", "Marketing", "Sales", "Engineering", "Finance", "Operations"]
    regions = ["North America", "Europe", "Asia", "Middle East", "Africa", "Latin America"]
    n_to_add = 100 - len(df)
    synthetic = []
    for i in range(n_to_add):
        dept = np.random.choice(departments, p=[0.12, 0.22, 0.22, 0.22, 0.12, 0.10])
        reg = np.random.choice(regions)
        perf = np.clip(np.random.normal(loc=78, scale=8), 40, 100)  # 40-100
        years = int(np.clip(np.random.normal(loc=6, scale=3), 0, 35))
        sat = np.clip(np.random.normal(loc=3.6, scale=0.7), 1.0, 5.0)
        emp_id = f"EMP{len(df)+i+1:03d}"
        synthetic.append([emp_id, dept, reg, round(perf, 2), years, round(sat, 1)])

    df2 = pd.DataFrame(synthetic, columns=df.columns)
    df_all = pd.concat([df, df2], ignore_index=True)
    return df_all

def main():
    df = load_employee_data()

    # Calculate frequency count for HR department
    hr_count = (df["department"] == "HR").sum()
    print(f"HR Department Count: {hr_count}")

    # Histogram of departments (categorical -> bar chart of counts)
    counts = df["department"].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    plt.bar(counts.index, counts.values)
    plt.title("Distribution of Employees by Department")
    plt.xlabel("Department")
    plt.ylabel("Count of Employees")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    # Save visualization
    plt.savefig("department_distribution.png", dpi=200, bbox_inches="tight")

if __name__ == "__main__":
    main()
