import requests
from pprint import pprint as print

API_KEY='177a32e40abbb362ba9a8aa9'

currency='RUB'
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS'

# Making our request
response = requests.get(url)
print(response.status_code)
res=response.json()
print(res)
print(res['conversion_rate'])
