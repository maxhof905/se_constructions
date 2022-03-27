"""turn Corpus do Português and Corpus del Español into one-sentence-per-line se corpus, compatible in format to the ud se_corpus"""

import re
import nltk
# nltk.download('punkt')

filter_words = [word.rstrip() for word in open('corpusdata_org/sp_noisy_words_filtered.txt')]  # words in the sp_text.txt ending in 'se' that should not be considered for the final corpus


def extract_sentences_pt(file):
    with open(file, 'r') as infile:
        with open('corpusdata_org/pt_text_se_corpus.txt', 'a') as outfile:
            print('opening ', outfile)
            for line in infile:
                line = re.sub('@@[0-9]+\\s', '', line)  # split source identification id
                sentences = nltk.sent_tokenize(line, language='portuguese')
                for sentence in sentences:
                    # enclitic uses of 'se' are already split in the input data: identify se based on whitespace characters
                    if len(re.findall(r'\sse\s', sentence)) == 1 and '@' not in sentence:
                        sentence = sentence.replace('"«', '«').replace('"»','»').replace('- ', ' ').replace('=$', ' ').replace('=', ' ')  # input torna- se,  output: torna se (alignes wiht stanza multi word tokenization)
                        outfile.write(sentence)
                        outfile.write('\n')
    print('wrote data to file')
    return None


def extract_sentences_es(file):
    with open(file, 'r') as infile:
        with open('corpusdata_org/sp_text_se_corpus.txt', 'a') as outfile:
            print('opening ', outfile)
            for line in infile:
                line = re.sub('@@[0-9]+\\s', '', line)  # split source identification id
                sentences = nltk.sent_tokenize(line, language='spanish')
                for sentence in sentences:
                    # 'se' can occur inside a token followed by another clitic 'decirselo' or token final after infinitive or imperative 'encontrarse'/'apurese-apurense' as well as as an individual token 'se'
                    if len(re.findall(r'(\bse\b|\Bse\b|\Bse(?=l.?.?\b))', sentence)) == 1 and '@' not in sentence:
                        if not any(word in sentence for word in filter_words):
                            if len(re.findall('[A-z]\\?[A-z]', sentence)) == 0:  # omit encoding errors (e.g coraz?n)
                                sentence = sentence.replace('"«', '«').replace('"»', '»').replace('=', ' ')
                                outfile.write(sentence)
                                outfile.write('\n')
    print('wrote data to file')
    return None


extract_sentences_pt('corpusdata_org/pt_text.txt')

extract_sentences_es('corpusdata_org/sp_text.txt')


