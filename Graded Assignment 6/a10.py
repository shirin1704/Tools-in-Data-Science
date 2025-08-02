import pandas as pd
from datetime import datetime

data = pd.read_csv('q-python-datetime-analysis.csv')
print(data)

formats = [
    "%a, %d %b %Y %H:%M:%S %Z",  # Tue, 20 Feb 2024 10:28:12 GMT
    "%d/%m/%Y %H:%M:%S",         # 08/02/2024 10:36:10
    "%Y-%m-%dT%H:%M:%S"          # 2024-01-01T10:32:41
]

def try_parse_datetime(value):
    for fmt in formats:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None  # or raise an error if you prefer strictness

# Apply parsing
data['Parsed_Timestamp'] = data['Timestamp'].apply(try_parse_datetime)

# Preview the result
print(data[['Timestamp', 'Parsed_Timestamp']])

data['Hour'] = data['Parsed_Timestamp'].dt.hour

print(data['Hour'].value_counts())
