import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('The small, barren planet also has a thin atmosphere that is 95 percent carbon dioxide.')
for i in doc:
    #print(i, i.pos_)
    print(dir(i))
    break
