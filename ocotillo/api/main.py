#!flask/bin/python
from flask import Flask
from pymongo import MongoClient
from flask import jsonify


app = Flask(__name__)
client = MongoClient('localhost',
                    username='root',
                    password='example',
                    # authSource='the_database',
                    authMechanism='SCRAM-SHA-256')

# exampl/api/v1/facts/mars
@app.route('/api/v1/<collection>/<subject>')
def get_documents(collection, subject, db='mars', objects=None, methods=['GET']):
    db_name = db
    db = client[db_name]
    collection = db[collection]
    result = []
    for row in collection.find({'subject': subject}):
        for fact in row['facts']:
            result.append({"object": fact['object']})
            
    return jsonify({'result': result})
            

if __name__ == '__main__':
    app.run(debug=True)
    