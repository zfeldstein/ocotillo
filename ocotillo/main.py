import spacy
from spacy.matcher import Matcher, PhraseMatcher

def print_ents(doc):
    for ent in doc.ents:
        print(ent.text, ent.label_)
        print('=' * 25)
    
nlp = spacy.load('en_core_web_sm')
doc = open('./data/mars-temp.txt').read()
doc = nlp(doc)


def extract_degrees_relations(doc):
    # merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    for money in filter(lambda w: w.ent_type_ == 'QUANTITY', doc):
        if money.dep_ in ('attr', 'dobj'):
            subject = [w for w in money.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations.append((subject, money))
        elif money.dep_ == 'pobj' and money.head.dep_ == 'prep':
            relations.append((money.head.head, money))
    return relations


relations = extract_degrees_relations(doc)
for r1, r2 in relations:
    print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))

# print_ents(doc)