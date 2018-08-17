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
    for subject, facts in db_data.items():
        subject_str = str(subject)
        document = {
        'subject': subject_str,
        'facts' : db_data[subject]
        }
        db['facts'].insert_one(document)

# doc ='The big blue planet reaches 9100 degrees farenheit.'
doc = 'The small red planet reaches 60 degrees farenheit. The big blue planet reaches 40 degrees farenheit.'

facts = db['facts']
# pprint.pprint(facts.find_one())
#


# wolf = facts.find({"subject": {"$in": ["planet", "D"]}})
# print(wolf)
for row in facts.find({"subject" : "planet"}):
    for fact in row['facts']:
        print(fact)

# cursor = db.facts.find({})
# for row in cursor:
#     print(row)
# cursor = planet.find({"facts":  ["big",
#             "blue",
#             "9100",
#             "degrees",
#             "farenheit"
#         ]})

# cursor = planet.find({"facts":  ["big",
#             "blue"
#         ]})

# # 
# pprint.pprint(facts)
# print([i for i in cursor])



# insert_documents(doc)
