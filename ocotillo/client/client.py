#!/usr/bin/env python
import requests
import argparse
import sys
import os

ACCOUNT = 'acct_01'
BASE_URL = 'http://localhost:5000/api/v1/{}'.format(ACCOUNT)

HEADERS = {'content-type': 'application/json'}
COMMANDS = ['docs']

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

def upload_doc(doc_name, doc_path):
    url = '{}/docs/{}'.format(BASE_URL,doc_name)
    files = {'file': open(doc_path, 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

parser = argparse.ArgumentParser()
# parser.add_argument("-s", "--search", action="store",
#                     help="the document db to search")
# parser.add_argument("-sb", "--subject", action='store', 
#                     help="Person place or thing you want data about. ( -sb Earth)")
# parser.add_argument("-f", "--facts", action='store', 
#                     help="information relating to the subject (-f oceans) ")
# parser.add_argument("-d", "--docs", action='store_true', 
#                     help="List all created document databases ( --docs ) ")
# parser.add_argument("-u", "--upload", action='store', 
#                     help="Upload file to be parsed ( --upload /file.pdf ) ")
parser.add_argument("docs",
                    help="docs command followed by action ( docs list ) ")
subparsers = parser.add_subparsers(dest='action')
list_parser = subparsers.add_parser("list")

upload_parser = subparsers.add_parser("upload")
upload_parser.add_argument("-f", "--file", dest="upload_file",
                           help='/path/to/file for upload/parsing')
upload_parser.add_argument("-n", "--name", dest="doc_name",
                           help='Name of endpoint you want created ( docs upload --file /file -n roman_history) ')

search_parser = subparsers.add_parser("search")

# # If no argument supplied or not valid display help
if sys.argv[1] not in COMMANDS:
    sys.argv.append('--help')

args = parser.parse_args()

# if args.docs:
    # upload_doc(args.upload)
# if args.search:
#     search_doc()
if args.docs == 'docs':
    if args.action == 'list':
        list_docs()
    if args.action == 'upload':
        doc_path = os.path.abspath(args.upload_file)
        upload_doc(args.doc_name, doc_path)
        