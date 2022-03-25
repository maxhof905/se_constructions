""" here torna-se is plit to torna- se. In bosque it is kept (torna-se) and in gsd we find torna - se"""
# todo these sentences are tokenized (Em a verdade) there is not much sense in reordering punctuation

import re
import nltk
from nltk.tokenize import RegexpTokenizer

clean_sentences = []
punct = '.,?%!()$€'
with open('text.txt') as file:
    for line in file:
        line = re.sub('@@[1-9]+\\s', '', line)
        sentences = nltk.sent_tokenize(line, language="portuguese")
        for sentence in sentences:
            if ' se ' in sentence and '@ @ @ @ @ @ @ @ @ @' not in sentence: # todo use regex to filter for the sentences that contain the se pattern only once
                sentence = sentence.replace('"«', '«').replace('"»', '»')
                for char in punct:
                    if char in sentence:
                        sentence = sentence.replace(' '+char, char)
                if '-' in sentence:
                    sentence = sentence.replace('- ', '-')
                if '«' in sentence:
                    sentence = sentence.replace('« ', '«')
                clean_sentences.append(sentence)

print(len(clean_sentences))

