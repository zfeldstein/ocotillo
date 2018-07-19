import pymysql
import spacy
from spacy.symbols import nsubj, VERB

db = pymysql.connect(host='localhost',
                     user='root',
                     password='example')

# string = 'The small, barren planet also has a thin atmosphere that is 95 percent carbon dioxide.'
string = 'The small red planet reaches 90 degrees farenheit.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(string)

# for chunk in doc.noun_chunks:
#     print("Chunk Text:  %s" % (chunk.text))
#     print("Chunk root Text:  %s" % (chunk.root.text))
#     print("Chunk Root Dep: %s" % (chunk.root.dep_))
#     print("Chunk Root Head Text: %s" % (chunk.root.head.text))
#     print('=' * 35)
#

# verbs = set()
# nouns = set()
# # The scope of this loop is possible_subject == one sentence at a time. 
# for possible_subject in doc:
#     if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
#         verbs.add(possible_subject.head)
#         nouns.add(possible_subject)
# print(verbs)
# print(nouns)


#Find a subject

knowledge = {}

# knowledge = [
    # {'planet' : ['red', 'small'] }
    # ]

# ROOT =verb
root = [token for token in doc if token.head == token][0]

# print(root)

#Subject = Noun
subject = list(root.lefts)[0]


# 
# print(subject)

knowledge[subject] = []
for descs in subject.subtree:
    
    if descs.pos_ == 'ADJ':
        knowledge[subject].append(descs)
        
print(knowledge)
    
    # print(descs, descs.pos_ )

# for descendant in subject.subtree:
#      # assert subject is descendant or subject.is_ancestor(descendant)
#     print(descendant.text, descendant.dep_, descendant.n_lefts,
#            descendant.n_rights,
#            [ancestor.text for ancestor in descendant.ancestors])

#           print([ancestor.text for ancestor in descendant.ancestors])
