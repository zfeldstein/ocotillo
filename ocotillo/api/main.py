#!flask/bin/python
import sys
import logging
from flask import Flask
from docs import docs
from pymongo import MongoClient
from flask import jsonify
from flask import request

app = Flask('fact_find')
# BASE_URL = '/api/v1'
client = MongoClient('localhost',
                    username='root',
                    password='example',
                    # authSource='the_database',
                    authMechanism='SCRAM-SHA-256')
def jwrap(key,values):
    json_obj = jsonify({key: values})
    return json_obj

def log(var, msg='Here is your var'):
    app.logger.info("%s %s" % ( msg, var))
    

# exampl/api/v1/mars/subject
@app.route('/api/v1/<acct>/<doc_name>')
def get_facts(acct, doc_name, methods=['GET']):
    content = request.get_json()
    if content:
        #Must specify a subject to query
        if content.get('subject') == None:
            return jwrap('error', 'specify subject in request')
        db = client[acct]
        collection = db[doc_name]
        result = []
        if content.get('object') != None:
            results = collection.find({'subject': content['subject'], 'facts.object': content['object']})
        else:
            results = collection.find({'subject': content['subject']})
        for row in results:
            for fact in row['facts']:
                result.append({"object": fact['object']})
                
        # return jsonify({'facts': result})
        return jwrap('facts', result)
    else:
        app.logger.warn("No json found %s" % content)        
        return "NoJsonError"
    
@app.route('/api/v1/<acct>/docs', methods=['GET'])
def list_docs(acct):
    db = client[acct]
    collections = db.list_collection_names()
    return jwrap('docs' , collections  )
            
# DOC parse and upload 
@app.route('/api/v1/<acct>/docs/<doc_name>', methods=['POST'])
def upload_file(acct, doc_name):
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
    doc = request.files['file']
    doc_path = './uploads/docs/{}/{}'.format(acct,doc_name)
    open(doc_path, 'w')
    doc.save(doc_path)
    return "Doc {} successfully saved".format(doc_path)

if __name__ == '__main__':
    app.run(debug=True)
    