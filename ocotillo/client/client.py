import requests
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-e", "--endpoint", action="store",
#                     help="Person place or thing you want data about.")
# parser.add_argument()
# args = parser.parse_args()
# 
# if not args.endpoint or args.endpoint not in ['facts']:
#     exit('no endpoint argument specified')

URL = 'http://localhost:5000/api/v1/acct_01/space_doc'

HEADERS = {'content-type': 'application/json'}
payload = {"subject": "Mars", 'object': 'Sun'}
# payload = {"subject": "Mars"}
r = requests.get(URL, headers=HEADERS, json=payload)
print(r.text)