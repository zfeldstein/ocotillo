import spacy
import json
from pymongo import MongoClient


client = MongoClient('localhost',
                    username='root',
                    password='example',
                    # authSource='the_database',
                    authMechanism='SCRAM-SHA-256')




# string = 'The small red planet reaches 60 degrees farenheit. The big blue planet reaches 40 degrees farenheit.'
string ='The big blue planet reaches 9100 degrees farenheit.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(string)

# doc = open('./data/mars-temp.txt').read()
# doc = nlp(doc)

knowledge = {}
root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]

facts = []

for chunk in doc.noun_chunks:
    # print(type(chunk))
    # for token in chunk:
        # if token.pos_ in ['DET'] or token.text == subject.text:
            # del chunk[token.text]
    facts.append(chunk.text)


facts = ' '.join(facts)
facts = nlp(facts)
facts.vocab["DET"].is_stop = True
final_facts = []
for i in facts:
    if i.pos_ in ['DET'] or i.text == subject.text:
        pass
    else:
        # print(i.text)
        final_facts.append(i.text)
        


        
# knowledge[subject] = facts
# facts = [fact for fact in final_facts if fact != 'The']
knowledge[subject] = final_facts
# collection_name = str(subject)
db = client['planet']
document = {
    str(subject) : [
        knowledge[subject]
    ]
}
# knowledge['subject'] = json.dumps(knowledge[subject])
# db.inventory.insert_one(knowledge[subject])
db.inventory.insert_one(document)


# print(knowledge)
# for i in knowledge:
#     print("Details about a %s" % (i))
#     for x in knowledge[i]:
#         print("facts %s" % (x))
    
    


     