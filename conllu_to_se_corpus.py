""" file to convert conllu files to se corpus in tab separated format"""

from typing import List
import pandas as pd
import os
#%%


def get_se_dict(infile):
    """extract the whole sentences containing 'se' from the treebank and save the dependency tag for se as label"""
    sentences = []
    lines = []
    se_dict = dict()
    new_line = '\n'
    se_sentences = []
    sentence_index = 0

    with open(infile, 'r', encoding='utf-8') as file:
        for line in file:
            if line != new_line:
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
                if elem.startswith('# sent_id ='):
                    # todo replace instead of strip
                    corpus_id = elem.rstrip().strip('# sent_id =')  # keep track of sentence ids from the treebank
                if elem.startswith('# text ='):
                    # replace supra segmental characters (parenthesis and commas influence argument structure > keep)
                    # inconsistent use of dashes > replace with empty string
                    text = elem.strip('# text =').rstrip().replace('«', '').replace('»', '').replace('-- ', '').replace('\'', '').replace('"', '').replace('- -', '')

                if '\tse\t' in elem.lower():  # match the word column of .conllu format
                    counter += 1
                    dep_tag = elem.split('\t')[7]
                    # pos_tag = elem.split('\t')[4]  # all labeled as p0000000

            if counter == 1:  # eliminate sentences where se occurs twice
                sentence_index += 1
                se_dict[sentence_index] = [corpus_id, text, dep_tag]

            if counter > 1:  # store the sentences that contain double se in a file
                with open('double_se_occurrences.txt', 'a') as outfile:
                    outfile.write(text)
                    outfile.write('\n')
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

        df = pd.DataFrame.from_dict(get_se_dict(filename), orient='index', columns=['corpus_id', 'text', 'dependency_tag'])
        print('\n')
        print(file)
        print(df.dependency_tag.value_counts())  # keep track of the dependency tags used
        print(df.shape)

        # # print(df.shape, outfile)
        df.to_csv(outfile, header=False, sep='\t',  encoding='utf-8', index=False)


#%%
# test procedure on a sinle file
# filename = 'ud/conllu/es_gsd-ud-test.conllu'
# df = pd.DataFrame.from_dict(get_se_dict(filename), orient='index', columns=['corpus_id', 'text', 'dependency_tag'])
# print('\n')
# print(df.dependency_tag.value_counts())
# print(df.shape)
#%%

# def get_data_splits(directory:str):
#     """ merge gsd and bosque splits"""
#     for root, dirs, files in os.walk(directory):
#             dev_data = [pd.read_table(root+'/'+file) for file in files if 'dev' in file]
#             df_dev = pd.concat(dev_data)
#             print(df_dev, df_dev.shape)

#%%

# todo averiguar porque es que desaparce el inicio del index en pt