import spacy
import stanza

text = '¡Me dieron 20$ por haberselo dicho!'
text_pt = 'O João deita-se muito cedo'
tokenized_text = 'Depende de vocês o quanto se importam em acender- la e emitir- la .'

# stanza.download("es")
stanza.download('pt')
nlp = stanza.Pipeline(lang='pt', processors='tokenize, mwt')

doc = nlp(tokenized_text)
for token in doc.sentences[0].tokens:
    # print(' '.join([word.text for word in token.words]))
    print(*[word.text for word in token.words])
    # print(f'token: {token.text}\twords: {", ".join([word.text for word in token.words])}')