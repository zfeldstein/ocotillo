#!/usr/bin/env python
import requests
import argparse
import sys
import os


ACCOUNT = 'acct_01'
BASE_URL = 'http://localhost:5000/api/v1/{}'.format(ACCOUNT)

HEADERS = {'content-type': 'application/json'}
COMMANDS = ['docs']

def api_call(url, method='get', files=None, data=None, json=None, headers=HEADERS):
    if method == 'get':
        r = requests.get(url, headers=headers, json=json)
    if method == 'post':
        print(files)
        # r = requests.post(url, files=files, data=data, headers=headers, json=json)
        r = requests.post(url, files=files, json=json)
    if method == 'delete':
        r = requests.delete(url)
    return r.text

def delete_doc():
    url = '{}/docs/{}'.format(BASE_URL, args.doc_name)
    print(api_call(url, method='delete'))

def search_doc():
    # url ='%s/%s' % (BASE_URL, args.search)
    url = '{}/docs/{}/search'.format(BASE_URL, args.doc_name)
    payload = {"subject": args.search_sub, 'facts': args.facts}
    print(api_call(url, 'post', json=payload))
    
def list_docs():
    url = '{}/docs'.format(BASE_URL)
    print(api_call(url))

def upload_doc(doc_name, doc_path, file_type):
    url = '{}/docs/{}'.format(BASE_URL,doc_name)
    files = {'file': open(doc_path, 'rb')}
    # headers = {'content-type': 'multipart/form-data'}
    meta_data = {"name": doc_name, "file_type": file_type}
    print(api_call(url, method='post',  files=files))

parser = argparse.ArgumentParser()
parser.add_argument("docs",
                    help="docs command followed by action ( docs list ) ")
subparsers = parser.add_subparsers(dest='action')
list_parser = subparsers.add_parser("list")

upload_parser = subparsers.add_parser("upload")
upload_parser.add_argument("-f", "--file", dest="upload_file",
                           help='/path/to/file for upload/parsing')
upload_parser.add_argument("-n", "--name", dest="doc_name",
                           help='Name of endpoint you want created ( docs upload --file /file -n roman_history) ')
upload_parser.add_argument("-t", "--type", dest="file_type",
                           help='type of file to upload if not specified client will assume txt file \
                           supported types are txt and pdf', default="txt")

search_parser = subparsers.add_parser("search")
search_parser.add_argument("-sb", "--subject", dest='search_sub', 
                     help="Person place or thing you want data about. ( -sb Earth)")
search_parser.add_argument("-f", "--facts", dest='facts', 
                    help="information relating to the subject (-f oceans) ")
search_parser.add_argument("doc_name", help="Name of doc database you want deleted")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("doc_name", help="Name of doc database you want deleted")
delete_parser.add_argument("-y", "--yes", dest="delete_yes", action='store_true',
                           help='suppress y/n prmopt on deletes')

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
        upload_doc(args.doc_name, doc_path, args.file_type)
    # Delete document, confirm delete before proceeding.
    if args.action == 'delete':
        if args.delete_yes:
            delete_doc()
        else:
            confirm = input("Type yes to confirm deleteing doc\n")
            if confirm.lower() == 'yes':
                delete_doc()
    if args.action == 'search':
        search_doc()
        