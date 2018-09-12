import spacy
import json
import slate
import pprint
from pymongo import MongoClient


client = MongoClient('localhost',
                    username='root',
                    password='example',
                    authMechanism='SCRAM-SHA-256')
nlp = spacy.load('en_core_web_sm')

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
        if root:
            print('AYO')
            print(root)
            if len(list(root.lefts)) < 1:
                continue
            subject = list(root.lefts)[0]        
        else:
            continue
        if not clean_subject(subject):
            continue
        #Gather Facts
        facts = []
        for chunk in sent.noun_chunks:
            facts.append(chunk.text)
        clean_facts = fact_clean(facts,subject)
        knowledge[subject] = clean_facts
    return knowledge

def clean_doc(doc):
    pass

def create_doc_col(db, doc_name, doc, file_type='txt'):
    # PDFSyntaxError
    if file_type == 'pdf':
        with open(doc, 'rb') as f:
            doc = slate.PDF(f)
            doc = str(doc)
    elif file_type == 'txt':
        doc = open(doc).read()
    db = client[db]
    # doc = clean_doc(doc)
    db_data = parse_facts(doc)
    for subject, facts in db_data.items():
        subject_str = str(subject)
        document = {
        'subject': subject_str,
        'facts' : db_data[subject]
        }
        db[doc_name].insert_one(document)
    #TODO add real check and return real value
    return "Sucesfully created doc database"