import spacy
from spacy.matcher import Matcher, PhraseMatcher

def print_ents(doc):
    for ent in doc.ents:
        print(ent.text, ent.label_)
        print('=' * 25)
    
nlp = spacy.load('en_core_web_sm')
doc = open('./data/mars-temp.txt').read()
doc = nlp(doc)


def extract_relations(doc, ent_labels=['QUANTITY']):
    # merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    
    for label in ent_labels:
        # loop through all tokens in doc, if token.ent_type == entitity label
        # look at that tokens properties
        for ent in filter(lambda w: w.ent_type_ == label, doc):
            #print(ent.dep_, ent.text, ent.ent_type_)
            if ent.dep_ in ('ccomp', 'poss'):
                subject = [w for w in ent.head.lefts if w.dep_ == 'nsubj']
                if subject:
                    subject = subject[0]
                    relations.append((subject, ent))
            elif ent.dep_ == 'pobj' and ent.head.dep_ == 'prep':
                relations.append((ent.head.head, ent))
    for r1, r2 in relations:
        print('{:<10}\t{}\t{}\t{}'.format(r1.text, r2.dep_, r2.ent_type_, r2.text))
    return relations

ent_labels = ['ORG', 'GPE', 'MONEY', 'LOC',  'PERSON', 'QUANTITY', 'NORP',
              'FAC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE',
              'DATE', 'TIME', 'PERCENT', 'ORDINAL', 'CARDINAL',]
extract_relations(doc, ent_labels)
    # relations = extract_degrees_relations(doc, label)
    # for r1, r2 in relations:
        # print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))

# print_ents(doc)

# print('=' * 200)
# for i in doc[0:5]:
#     if i.ent_type:
# 
#         print(i.ent_type_, i.text)
# for i in doc.ents:
#     print('-' * 46)
#     print(i)
# for ent in filter(lambda w: w.ent_type_ == 'LOC', doc):
#     print(ent, ent.dep_)
