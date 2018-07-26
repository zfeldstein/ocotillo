import spacy

string = 'The small red planet reaches 90 degrees farenheit.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(string)

knowledge = {}
root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]

facts = []
for chunk in doc.noun_chunks:
    facts.append(chunk.text)


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


    