import random

import pandas as pd
from sklearn.metrics import cohen_kappa_score

#%%
""" 
spanish: expl:pv, expl:pass, expl:impers, iobj, obj, flat, fixed
portuguese: expl, nsubj, mark, expl:pass, iobj, obj, fixed, case, nmod

"""

#%%


def create_sample(infile_1, infile_2, infile_3, outfile_1, outfile_2):
    """ create annotation file from data splits"""
    with open(infile_1, 'r') as train, open(infile_2, 'r') as dev, open(infile_3, 'r') as test:
        with open(outfile_1, 'w') as sample_file, open(outfile_2, 'w') as true_file:
                train_lines = train.readlines()
                dev_lines = dev.readlines()
                test_lines = test.readlines()
                lines = train_lines + dev_lines + test_lines
                random_lines = random.sample(lines, 200)
                for line in random_lines:
                    true_file.write(line) # todo keep or dismiss label
                    sample_file.write(line.split('\t')[1] + '\n')
    return None

#%%


es_train = 'ud/es_data/es_ancora-ud-train.txt'
es_dev = 'ud/es_data/es_ancora-ud-dev.txt'
es_test = 'ud/es_data/es_ancora-ud-test.txt'
es_my_anno = 'ud/samples/es_ancora-ud-sample.txt'
es_ud_anno = 'ud/samples/es_ancora-ud-true.txt'
# create_sample(es_train, es_dev, es_test, es_sample, es_true)

pt_train = 'ud/pt_data/pt_bosque-ud-train.txt'
pt_dev = 'ud/pt_data/pt_bosque-ud-dev.txt'
pt_test = 'ud/pt_data/pt_bosque-ud-test.txt'
pt_my_anno = 'ud/samples/pt_bosque-ud-sample.txt'
pt_ud_anno = 'ud/samples/pt_bosque-ud-true.txt'
#create_sample(pt_train, pt_dev, pt_test, pt_sample, pt_true)


#%%
# check for missing tabs, labels and misspelled tags
df = pd.read_csv('ud/samples/pt_bosque-ud-sample.txt', sep='\t', names=['A', 'B'])
#%%
df.B.value_counts()
#%%

def get_label_column(infile):
    with open(infile) as file:
        labels = [line.split('\t')[-1].rstrip() for line in file.readlines()]
    return labels


#%%
#
es_y_ud_anno = get_label_column(es_ud_anno)
es_y_my_anno = get_label_column(es_my_anno)

pt_y_ud_anno = get_label_column(pt_ud_anno)
pt_y_my_anno = get_label_column(pt_my_anno)

es_iaa = cohen_kappa_score(es_y_ud_anno, es_y_my_anno)
pt_iaa = cohen_kappa_score(pt_y_ud_anno, pt_y_my_anno)

#%%

print(es_iaa, pt_iaa)

#%%