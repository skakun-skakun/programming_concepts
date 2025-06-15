import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_KEY = os.getenv("WEATHERAPI_KEY")
BASE_URL = "https://api.weatherapi.com/v1"

resp = requests.get(f"{BASE_URL}/forecast.json?key={API_KEY}&q=Kyiv&days=7")
# print(resp.status_code)

if (resp.status_code != 200):
    print("L, API responded with status code " + str(resp.status_code))
    exit(1)

data = {
    'temp': [],
    'wind_spread': []
}

for day in resp.json()['forecast']['forecastday']:
    for hour in day['hour']:
        data['temp'].append(hour['temp_c'])
        data['wind_spread'].append(hour['wind_kph'])

df = pd.DataFrame(data)
print(f"Max temp in 3 days: {df.loc[0:71, 'temp'].max()}")
print(f"Min temp in 3 days: {df.loc[0:71, 'temp'].min()}")
print(f"Avg temp in 3 days (rounded to 1-2 symbols after coma): {df.loc[0:71, 'temp'].mean().round(2)}")

wind_avg = df['wind_spread'].mean()
# print(f"Avg wind: {wind_avg}")
# print(df.loc[df['wind_spread'] > wind_avg])
print(f"Number of hours wind was more than avg: {len(df.loc[df['wind_spread'] > wind_avg])}")

