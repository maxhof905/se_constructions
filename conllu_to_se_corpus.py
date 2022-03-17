import pandas as pd
import csv
import os
#%%


def get_se_dict(infile):
    sentences = []
    lines = []
    se_dict = dict()
    new_line = '\n'
    se_sentences = []
    sentence_index = 0

    with open(infile, 'r', encoding='utf-8') as file:
        for line in file:
            if line != new_line:
                lines.append(line)
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
                if elem.startswith(('# sent_id =')):
                    corpus_id = elem.strip('# sent_id =').rstrip()
                if elem.startswith('# text ='):
                    # replace supra segmental characters (parenthesis and commas influence argument structure > kept)
                    # dashes are inconsistently > eliminated
                    text = elem.strip('# text =').rstrip().replace('«', '').replace('»', '').replace('-- ', '').replace('\'', '').replace('"', '').replace('- -', '')

                if '\tse\t' in elem.lower(): #match the word column of conllu format
                    counter += 1
                    dep_tag = elem.split('\t')[7]
                    # pos_tag = elem.split('\t')[4]  # all labeled as p0000000

            if counter == 1: # eliminate sentences where se occurs twice
                sentence_index += 1
                se_dict[sentence_index] = [corpus_id, text, dep_tag]

    return se_dict

#%%

directory = "ud/conllu"
data = []
for root, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        filename = (os.path.join(root, file))
        if 'es_' in filename:
            out_dir = 'ud/es_data/'
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
            outfile = out_dir + file[:-7] + '.txt'

        if 'pt_' in filename:
            out_dir = 'ud/pt_data/'
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
            outfile = out_dir + file[:-7] + '.txt'

        # print(outfile)
# filename = 'ud/pt_bosque/pt_bosque-ud-train.conllu'

        df = pd.DataFrame.from_dict(get_se_dict(filename), orient='index', columns=['corpus_id', 'text', 'dependency_tag'])
        print('\n')
        print(file)
        print(df.dependency_tag.value_counts())
        print(df.shape)

        # # print(df.shape, outfile)
        df.to_csv(outfile, header=False, sep='\t',  encoding='utf-8')
        #
        # print('\n', outfile, '\n', df[:-1].value_counts(), '\n') # keep track of the dependency tags used)

#%%

