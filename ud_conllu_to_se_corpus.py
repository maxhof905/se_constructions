""" file to convert conllu files to se corpus in tab separated format"""

import pandas as pd
import os
import stanza


def get_se_dict(infile, nlp):
    """extract the whole sentences containing 'se' from the treebank and save the dependency tag for se as label"""
    sentences = []
    lines = []
    se_dict = dict()
    se_sentences = []

    with open(infile, 'r', encoding='utf-8') as file:
        for line in file:
            if line != '\n':
                lines.append(line)  # sentences are separated by a newline
            else:
                sentences.append(lines)
                lines = []

        for sentence in sentences:
            for elem in sentence:
                if elem.startswith('# text =') and 'se' in elem:
                    se_sentences.append(sentence)

        for sentence in se_sentences:
            counter = 0
            for elem in sentence:
                # if elem.startswith('# sent_id ='):
                #     corpus_id = elem.rstrip()
                #     corpus_id = corpus_id.replace('# sent_id = ', '')
                if elem.startswith('# text ='):
                    # replace supra segmental characters (parenthesis and commas influence argument structure > keep)
                    # inconsistent use of dashes > replace with empty string
                    text = elem.strip('# text =').rstrip().replace('«', '').replace('»', '').replace('-- ', '').replace('\'', '').replace('"', '').replace('- -', '')

                if '\tse\t' in elem.lower():  # match the word column of .conllu format
                    counter += 1
                    dep_tag = elem.split('\t')[7]
                    # pos_tag = elem.split('\t')[4]  # all labeled as p0000000

            if counter == 1:  # eliminate sentences where se occurs twice
                tokenized_text = [word.text for sent in nlp(text).sentences for word in sent.words] # tokenize text to match other data
                tokenized_text = ' '.join(tokenized_text).replace(' - ', ' ') # handle verb- se, verb-se, verb se in input data
                se_dict[text] = [tokenized_text, dep_tag]

            if counter > 1:  # store the sentences that contain double se in a file
                with open('ud/double_se_occurrences.txt', 'a') as outfile:
                    outfile.write(text)
                    outfile.write('\n')
    return se_dict


# stanza.download(language)
nlp_es = stanza.Pipeline(lang='es', processors='tokenize, mwt')
nlp_pt = stanza.Pipeline(lang='pt', processors='tokenize, mwt')

directory = "ud/conllu"
data = []
for root, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        filename = (os.path.join(root, file))
        if 'es_' in filename:
            nlp = nlp_es
            out_dir = 'ud/es_data/'
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
            outfile = out_dir + file[:-7] + '.txt'

        if 'pt_' in filename:
            nlp = nlp_pt
            out_dir = 'ud/pt_data/'
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
            outfile = out_dir + file[:-7] + '.txt'

        df = pd.DataFrame.from_dict(get_se_dict(filename, nlp=nlp), orient='index')
        print('\n')
        print(file)
        print(df[1].value_counts())  # keep track of the dependency tags used
        print(df.shape)


        # # print(df.shape, outfile)
        df.to_csv(outfile, header=False, sep='\t',  encoding='utf-8', index=True)
