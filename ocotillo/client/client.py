#!/usr/bin/env python
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--search", action="store",
                    help="the document db to search")
parser.add_argument("-sb", "--subject", action='store', 
                    help="Person place or thing you want data about. ( -sb Earth)")
parser.add_argument("-f", "--facts", action='store', 
                    help="information relating to the subject (-f oceans) ")
args = parser.parse_args()

ACCOUNT = 'acct_01'
URL = 'http://localhost:5000/api/v1/%s/%s' % (ACCOUNT, args.search)

HEADERS = {'content-type': 'application/json'}
payload = {"subject": args.subject, 'object': args.facts}
r = requests.get(URL, headers=HEADERS, json=payload)
print(r.text)
