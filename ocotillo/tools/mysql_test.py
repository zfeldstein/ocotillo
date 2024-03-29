# import pymysql
import spacy
from spacy.symbols import nsubj, VERB

# db = pymysql.connect(host='localhost',
                     # user='root',
                     # port=49162)

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
# print(list(subject.conjuncts))



# chunk.root.text == Root noun of chunk i.e. planet, farenheit   (NOUN)
# chunk.root.head.text == Verb of noun chunk i.e. reaches (VERB)
# chunk.text  == actual NP chunk (FULL CHUNK

facts = []
for chunk in doc.noun_chunks:
    # print(chunk.root.text)
    # print('-' * 25)
    # print("VERB IS %s" % (chunk.root.head.text))
    # print(type(chunk
    # [print(i) for i in chunk.pos_]
    facts.append(chunk.text)
    # print('-' * 25)
    # print("adj IS %s" % (chunk.text))
    # print('-' * 25)
    # for decendents in chunk.root.subtree:
    #     print(decendents)



facts = ' '.join(facts)
facts = nlp(facts)
final_facts = []
for i in facts:
    if i.pos_ in ['DET'] or i.text == subject.text:
        pass
    else:
        final_facts.append(i.text)
        
knowledge[subject] = final_facts


print(knowledge)

# knowledge[subject] = []

# print(root.n_rights)


# for descs in subject.subtree:
#     # print(descs)
#     # for i in descs.ancestors:
#     #     print(i, i.pos_)
#     
#     if descs.pos_ == 'ADJ':
#         knowledge[subject].append(descs)
        
# print(knowledge[subject])
    
    # print(descs, descs.pos_ )

# for descendant in subject.subtree:
#      # assert subject is descendant or subject.is_ancestor(descendant)
#     print(descendant.text, descendant.dep_, descendant.n_lefts,
#            descendant.n_rights,
#            [ancestor.text for ancestor in descendant.ancestors])

#           print([ancestor.text for ancestor in descendant.ancestors])
