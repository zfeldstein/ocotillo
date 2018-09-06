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
parser.add_argument("-d", "--docs", action='store_true', 
                    help="List all created document databases ( --docs ) ")
parser.add_argument("-u", "--upload", action='store', 
                    help="Upload file to be parsed ( --upload /file.pdf ) ")
args = parser.parse_args()

ACCOUNT = 'acct_01'
BASE_URL = 'http://localhost:5000/api/v1/%s' % (ACCOUNT)

HEADERS = {'content-type': 'application/json'}

def api_call(url, payload=None, headers=HEADERS):
    r = requests.get(url, headers=HEADERS, json=payload)
    return r.text

def search_doc():
    url ='%s/%s' % (BASE_URL, args.search)
    payload = {"subject": args.subject, 'object': args.facts}
    print(api_call(url, payload))
    
def list_docs():
    url = '%s/docs' % ( BASE_URL)
    print(api_call(url))

def upload_doc(doc_path):
    url = '%s/docs/mars' % ( BASE_URL)
    files = {'file': open(doc_path, 'rb')}
    r = requests.post(url, files=files)
    print(r.text)
    
if args.upload:
    upload_doc(args.upload)
if args.search:
    search_doc()
if args.docs:
    list_docs()