import json
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

required_city = "Toronto"
location_url = "https://locator-service.api.bbci.co.uk/locations?" + urlencode({
    "api_key" : "AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv",
    "s": required_city,
    "stack" :"aws",
    "locale" : "en",
    "filter" : "international",
    "place-types" : "settlement,airport,district",
    "order" : "importance",
    "a" : "true",
    "format": "json"
})

#print(location_url)

result = requests.get(location_url).json()
#print(result)

url = "https://www.bbc.com/weather/" + result['response']['results']['results'][0]['id']
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

daily_summary = soup.find('div', attrs = {'class' : 'wr-day-summary'})
#print(daily_summary)

daily_summary_list = re.findall('[a-zA-Z][^A-Z]*', daily_summary.text)

datelist = pd.date_range(datetime.today(), periods = len(daily_summary_list)).tolist()

datelist = [datelist[i].date().strftime('%Y-%m-%d') for i in range(len(datelist))]

zipped = zip(datelist, daily_summary_list)

df = pd.DataFrame(list(zipped), columns=['date', 'summary'])

#print(df)

# Convert to dictionary and then to JSON
json_obj = df.set_index("date")["summary"].to_dict()

# Optional: convert to JSON string
json_str = json.dumps(json_obj, indent=2)

print(json_str)

#Output:
'''{
  "2025-06-21": "Sunny intervals and a moderate breeze",
  "2025-06-22": "Sunny and a moderate breeze",
  "2025-06-23": "Sunny and a moderate breeze",
  "2025-06-24": "Thundery showers and a gentle breeze",
  "2025-06-25": "Light rain showers and light winds",
  "2025-06-26": "Light rain showers and a gentle breeze",
  "2025-06-27": "Light rain showers and a gentle breeze",
  "2025-06-28": "Sunny intervals and a gentle breeze",
  "2025-06-29": "Sunny intervals and a gentle breeze",
  "2025-06-30": "Light cloud and a gentle breeze",
  "2025-07-01": "Sunny intervals and light winds",
  "2025-07-02": "Sunny and light winds",
  "2025-07-03": "Light rain and a gentle breeze",
  "2025-07-04": "Sunny intervals and light winds"
}'''
