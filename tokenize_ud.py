import stanza

text = 'Na nossa realidade é um projeto que estimule no jovem uma vida sem drogas, promovendo-se um comportamento construtivo.'
text_2 = 'Un Segunda B, un campo en mal estado, la presión de jugárselo todo a partido único y la motivación de unos y otros.'
text_3 = 'Concentre-se, Concentre - se, Concentre- se'

# stanza.download('pt')
# stanza.download('es')
# nlp = stanza.Pipeline(lang='pt', processors='tokenize, mwt')

# doc = nlp(text_2)
# for token in doc.sentences[0].tokens:
#     for word in token.words:
#         output.append(word.text)

# output = [token.text for sent in nlp(text).sentences for token in sent.tokens]
# output = [word.text for sent in nlp(text_3).sentences for word in sent.words]
# match = ' '.join(output).replace(' - ', ' ')
# print(match)
#
nlp_2 = stanza.Pipeline(lang='es', processors='tokenize, mwt, pos,lemma, depparse')
doc = nlp_2('Maria se iba con genios')
print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')