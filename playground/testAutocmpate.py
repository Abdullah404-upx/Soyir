import requests

#res = requests.get('http://127.0.0.1:5000/autocomplete/cat')

#print(res.text)
q = "this is really frustrating"

res = requests.post(f'http://127.0.0.1:5000/autocomplete/{q}')
print(res.text)
