from pymongo import MongoClient
client = MongoClient('localhost',
                    username='root',
                    password='example',
                    # authSource='the_database',
                    authMechanism='SCRAM-SHA-256')

db = client.planet

db.inventory.insert_one()