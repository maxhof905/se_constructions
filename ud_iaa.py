import random

import pandas as pd
from sklearn.metrics import cohen_kappa_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


#%%
""" 
spanish: expl:pv, expl:pass, expl:impers, iobj, obj, flat, fixed
portuguese: expl, nsubj, mark, expl:pass, iobj, obj, fixed, case, nmod

labels to drop:
spanish: flat, fixed
portuguese: expl:pass, case, mod
"""

#%%


def create_sample(infile_1, outfile_1, outfile_2):
    """ create annotation file from data splits"""
    with open(infile_1, 'r') as infile:
        with open(outfile_1, 'w') as sample_file, open(outfile_2, 'w') as true_file:
                lines = infile.readlines()
                random_lines = random.sample(lines, 100)
                for line in random_lines:
                    true_file.write(line)
                    sample_file.write(line.split('\t')[0] + '\n')
    return None


def get_label_column(infile):
    with open(infile) as file:
        labels = [line.split('\t')[-1].rstrip() for line in file.readlines()]
    return labels

#%%

es_train = 'ud/es_data/es_ancora-ud-train.txt'
es_dev = 'ud/es_data/es_ancora-ud-dev.txt'
es_test = 'ud/es_data/es_ancora-ud-test.txt'
es_my_anno = 'ud/samples/es_ancora-ud-sample.txt'
es_ud_anno = 'ud/samples/es_ancora-ud-true.txt'


train = pd.read_csv(es_train, sep='\t', names=['text', 'tokenized_text', 'se_label'])
train.drop(columns=['text'], inplace = True)
dev = pd.read_csv(es_dev, sep='\t', names=['text', 'tokenized_text', 'se_label']) # colab
dev.drop(columns=['text'], inplace = True)
test = pd.read_csv(es_test, sep='\t', names=['text', 'tokenized_text', 'se_label']) # colab
test.drop(columns=['text'], inplace = True)
se_corpus = pd.concat([train, dev, test])
se_corpus = se_corpus.drop(se_corpus[(se_corpus['se_label'] == 'flat')].index)
se_corpus = se_corpus.drop(se_corpus[(se_corpus['se_label'] == 'fixed')].index)
se_corpus.to_csv('ud/samples/es_se_corpus', index=False,  sep='\t')

es_corpus = 'ud/samples/es_se_corpus'

create_sample(es_corpus, es_my_anno, es_ud_anno)

#%%
pt_train = 'ud/pt_data/pt_bosque-ud-train.txt'
pt_dev = 'ud/pt_data/pt_bosque-ud-dev.txt'
pt_test = 'ud/pt_data/pt_bosque-ud-test.txt'
pt_my_anno = 'ud/samples/pt_bosque-ud-sample.txt'
pt_ud_anno = 'ud/samples/pt_bosque-ud-true.txt'

# filter out labels
train = pd.read_csv(pt_train, sep='\t', names=['text', 'tokenized_text', 'se_label'])
train.drop(columns=['text'], inplace = True)
dev = pd.read_csv(pt_dev, sep='\t', names=['text', 'tokenized_text', 'se_label']) # colab
dev.drop(columns=['text'], inplace = True)
test = pd.read_csv(pt_test, sep='\t', names=['text', 'tokenized_text', 'se_label']) # colab
test.drop(columns=['text'], inplace = True)
se_corpus = pd.concat([train, dev, test])
se_corpus = se_corpus.drop(se_corpus[(se_corpus['se_label'] == 'expl:pass')].index)
se_corpus = se_corpus.drop(se_corpus[(se_corpus['se_label'] == 'case')].index)
se_corpus = se_corpus.drop(se_corpus[(se_corpus['se_label'] == 'nmod')].index)
se_corpus.to_csv('ud/samples/pt_se_corpus', index=False,  sep='\t')

pt_corpus = 'ud/samples/pt_se_corpus'
create_sample(pt_corpus, pt_my_anno, pt_ud_anno)

#%%
# do manual annotations
#
#%%
# check for missing tabs, labels and misspelled tags > nan values will appear in df
pt_df= pd.read_csv('ud/samples/pt_bosque-ud-sample.txt', sep='\t', names=['A', 'B'])

#%%
# check for missing tabs, labels and misspelled tags > nan values will appear in df
es_df= pd.read_csv('ud/samples/es_ancora-ud-sample.txt', sep='\t', names=['A', 'B'])

#%%

es_y_ud_anno = get_label_column(es_ud_anno)
es_y_my_anno = get_label_column(es_my_anno)

pt_y_ud_anno = get_label_column(pt_ud_anno)
pt_y_my_anno = get_label_column(pt_my_anno)

es_iaa = cohen_kappa_score(es_y_ud_anno, es_y_my_anno)
pt_iaa = cohen_kappa_score(pt_y_ud_anno, pt_y_my_anno)

#%%

print(es_iaa, pt_iaa)
# 0.6968778417702334 0.6529873264936632



#%%
fig, ax = plt.subplots(figsize=(12, 10))
plt.grid(False)
ConfusionMatrixDisplay.from_predictions(es_y_ud_anno, es_y_my_anno, ax=ax, cmap='binary')
ax.set_xticklabels(ax.get_xticklabels(),
                          rotation=45,
                          horizontalalignment='right')
plt.savefig('ancora_cfm.png')
plt.tight_layout()
plt.show()

#%%
fig, ax = plt.subplots(figsize=(12, 10))
plt.grid(False)
ConfusionMatrixDisplay.from_predictions(pt_y_ud_anno, pt_y_my_anno, ax=ax, cmap='binary')
ax.set_xticklabels(ax.get_xticklabels(),
                          rotation=45,
                          horizontalalignment='right')
plt.savefig('bosque_cfm.png')
plt.tight_layout()
plt.show()