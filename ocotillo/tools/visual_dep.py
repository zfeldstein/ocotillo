import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
#doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")
doc = open('../data/mars-temp.txt').read()
doc = nlp(doc)
#displacy.render(doc, style='dep', jupyter=True)
displacy.serve(doc, style='dep')
