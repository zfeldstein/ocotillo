import spacy
from spacy.symbols import nsubj, VERB

string = 'The small red planet reaches 90 degrees farenheit.'
nlp = spacy.load('en_core_web_sm')

doc = nlp(string)

sentences = list(doc.sents)

spacy.displacy.serve(doc, style='dep')

# for sentence in sentences:
    # print(sentence.root)
#     
# root_token = sentences[0].root
# for child in root_token.children:
#     print(child, child.dep_)
#     if child.dep_ == 'nsubj':
#         subj = child
#         # print(subj)
#     if child.dep_ == 'dobj':
#         obj = child
#         # print(obj)


# print(list(obj.children))
# print('=' * 35)
# print(subj)
# print(list(subj.children))