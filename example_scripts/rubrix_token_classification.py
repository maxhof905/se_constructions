import rubrix as rb
import stanza

# Loading a cool Obrint Pas lyric
input_text = "Se buscan camareros. Los niños siempre se ensucian."

# Downloading our model, in case we don't have it cached
stanza.download("es")

# Creating the pipeline
nlp = stanza.Pipeline(lang="es", processors="tokenize,mwt,pos,lemma,depparse")

# Analizing the input text
doc = nlp(input_text)

# Creating the prediction entity as a list of tuples (tag, start_char, end_char)
prediction = [
    (word.deprel, token.start_char, token.end_char)
    for sent in doc.sentences
    for token in sent.tokens
    for word in token.words
]
# print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')

# Building a TokenClassificationRecord
record = rb.TokenClassificationRecord(
    text=input_text,
    tokens=[word.text for sent in doc.sentences for word in sent.words],
    prediction=prediction,
    prediction_agent="stanza/spanish",
)

# Logging into Rubrix
rb.log(records=record, name="stanza-spanish-dep")