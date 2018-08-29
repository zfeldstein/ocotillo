import spacy
import json
import pprint
from pymongo import MongoClient


client = MongoClient('localhost',
                    username='root',
                    password='example',
                    # authSource='the_database',
                    authMechanism='SCRAM-SHA-256')
db_name = 'mars'
db = client[db_name]

# string = 'The small red planet reaches 60 degrees farenheit. The big blue planet reaches 40 degrees farenheit.'
nlp = spacy.load('en_core_web_sm')

# doc = open('./data/mars-temp.txt').read()
# doc = nlp(doc)

def fact_clean(facts, subject):
    #Clean Facts remove subject and det's
    facts = ' '.join(facts)
    facts = nlp(facts)
    final_facts = []
    for i in facts:
        if i.pos_ in ['DET', 'PUNCT'] or i.text == subject.text :
            pass
        else:
            final_facts.append({"object" : i.text})
    return final_facts

def clean_subject(subject):
    invalid_subjects = ['ADP']
    if subject.pos_ in invalid_subjects:
        return None
    else:
        return subject
    

#TODO Change to filename as first arg
def parse_facts(doc):
    doc = nlp(doc)
    knowledge = {}
    for sent in doc.sents:
        root = [token for token in sent if token.head == token][0]
        subject = list(root.lefts)[0]
        subject = clean_subject(subject)
        if not subject:
            continue
        #Gather Facts
        facts = []
        for chunk in sent.noun_chunks:
            facts.append(chunk.text)
        clean_facts = fact_clean(facts,subject)
        knowledge[subject] = clean_facts
    return knowledge

def insert_documents(doc):    
    db_data = parse_facts(doc)
    for subject, facts in db_data.items():
        subject_str = str(subject)
        document = {
        'subject': subject_str,
        'facts' : db_data[subject]
        }
        db['facts'].insert_one(document)
        
def get_documents(db, collection, subject, objects=None):
    # print(subject)
    collection = db[collection]
    # ({'subject': subject, 'facts.object' : objects})
    for row in collection.find({'subject': subject, 'facts.object': 'Sun'}):
        for i in row['facts']:
            print(i['object'])

# doc ='The big blue planet reaches 9100 degrees farenheit.'
doc = 'The small red planet reaches 60 degrees farenheit. The big blue planet reaches 40 degrees farenheit.'


docs = get_documents(db,'facts','Mars', 'Mars')



# doc = open('./data/mars-temp.txt').read()
doc = open('data/wiki-mars.txt').read()



# insert_documents(doc)
