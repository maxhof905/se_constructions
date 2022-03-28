import random
from sklearn.metrics import cohen_kappa_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plot
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import seaborn as sns

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
es_sample = 'ud/samples/es_ancora-ud-sample.txt'
es_true =  'ud/samples/es_ancora-ud-true.txt'
# create_sample(es_train, es_dev, es_test, es_sample, es_true)

pt_train = 'ud/pt_data/pt_bosque-ud-train.txt'
pt_dev = 'ud/pt_data/pt_bosque-ud-dev.txt'
pt_test = 'ud/pt_data/pt_bosque-ud-test.txt'
pt_sample = 'ud/samples/pt_bosque-ud-sample.txt'
pt_true = 'ud/samples/pt_bosque-ud-true.txt'
create_sample(pt_train, pt_dev, pt_test, pt_sample, pt_true)

#%%

def get_label_column(infile):
    with open(infile) as file:
        labels = [line.split('\t')[-1].rstrip() for line in file.readlines()]
    return labels


#%%
#
es_y_true = get_label_column(es_true)
es_y_pred = get_label_column(es_sample)

pt_y_true = get_label_column(pt_true)
pt_y_pred = get_label_column(pt_sample)

# print(y_true)
# print(y_pred)

es_iaa = cohen_kappa_score(es_y_true, es_y_pred)
pt_iaa = cohen_kappa_score(pt_y_true, pt_y_pred)

#%%
cm = confusion_matrix(es_y_true, es_y_pred)  # todo
f = sns.heatmap(cm, annot=True, fmt='d')