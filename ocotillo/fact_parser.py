import spacy
import json
from pymongo import MongoClient


client = MongoClient('localhost',
                    username='root',
                    password='example',
                    # authSource='the_database',
                    authMechanism='SCRAM-SHA-256')




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
        if i.pos_ in ['DET'] or i.text == subject.text:
            pass
        else:
            # print(i.text)
            final_facts.append(i.text)
    return final_facts

#TODO Change to filename as first arg
def parse_facts(doc):
    doc = nlp(doc)
    knowledge = {}
    root = [token for token in doc if token.head == token][0]
    subject = list(root.lefts)[0]
    #Gather Facts
    facts = []
    for chunk in doc.noun_chunks:
        facts.append(chunk.text)
    clean_facts = fact_clean(facts,subject)
    knowledge[subject] = clean_facts
    return knowledge

def insert_documents(doc):    
    db_data = parse_facts(doc)
    db_name = 'mars'
    db = client[db_name]
    for subject, facts in db_data.items():
        print(subject,facts)
        collection_name = str(subject)
        document = {
        'facts' : [
            db_data[subject]
            ]
        }
        db[collection_name].insert_one(document)

doc ='The big blue planet reaches 9100 degrees farenheit.'
doc = 'The small red planet reaches 60 degrees farenheit. The big blue planet reaches 40 degrees farenheit.'
insert_documents(doc)

     