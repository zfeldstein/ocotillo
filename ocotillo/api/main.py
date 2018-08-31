#!flask/bin/python
import sys
import logging
from flask import Flask
from pymongo import MongoClient
from flask import jsonify
from flask import request


# app = Flask(__name__)
app = Flask('fact_find')
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
@app.route('/api/v1/<db>/subject')
def get_subjects(db, collection='facts', methods=['GET']):
    content = request.get_json()
    if content:
        #Must specify a subject to query
        if content.get('subject') == None:
            return jwrap('error', 'specify subject in request')
        db_name = db
        db = client[db_name]
        collection = db[collection]
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
            

if __name__ == '__main__':
    app.run(debug=True)
    