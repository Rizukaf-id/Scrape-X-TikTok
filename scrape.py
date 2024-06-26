import requests

payload = { 'api_key': '4876b6a9fbc1f70d2b61c290cb57ebef', 'url': 'https://x.com/search?q=e%20commerce&src=typed_query' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
