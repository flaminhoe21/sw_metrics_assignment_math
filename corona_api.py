import json
import requests


response = requests.get('https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?search=india')

if response.status_code == 200:
    print('Success: Page Loaded!')
elif response.status_code == 404:
    print('Error: Page Not Found!')

print(response.status_code)
print(response.content)
sh = response.json()

for n in sh['data']:
    print(['new_cases'])