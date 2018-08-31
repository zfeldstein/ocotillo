import requests

URL = 'http://localhost:5000/api/v1/mars/subject'

HEADERS = {'content-type': 'application/json'}
payload = {"subject": "Mars", 'object': 'Sun'}
# payload = {"subject": "Mars"}
r = requests.get(URL, headers=HEADERS, json=payload)
print(r.text)