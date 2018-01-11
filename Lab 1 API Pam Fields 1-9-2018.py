import requests

import os

key = os.environ['fixer_key']

base_url = "https://fixer.io/latest?symbols="

currency = input('What is the first country to compare currency exchanges? Please use the three letter abbreviation ')

params = {'fixer_key', 't' : currency}
data = dict(dict(requests.get("https://api.fixer.io/2018-01-10").json()).get("rates")).get(currency)

print(data)

print("Current Exchange rate with Euro:")
print(data['rates'][0]['Value'])
