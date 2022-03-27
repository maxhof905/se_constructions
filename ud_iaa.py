import random
from sklearn.metrics import cohen_kappa_score

# todo merge together all of gsd and then draw sample
# todo decide wheteher to show labels to anotator or not
# todo work with predefines set of labels? -- define the set of possible labels >> se article or ud docs
#%%

def create_sample(infile, outfile_1, outfile_2):
    with open(infile, 'r') as file:
        with open(outfile_1, 'w') as sample_file:
            with open(outfile_2, 'w') as true_file:
                random_lines = random.sample(file.readlines(), 200)
                for line in random_lines:
                    true_file.write(line) # todo keep or dismiss label
                    sample_file.write(line.split('\t')[1] + '\n')
    return infile, outfile_1, outfile_2
#%%

es_gsd = create_sample('ud/es_data/es_gsd-ud-train.txt', 'ud/samples/es_gsd-ud-train-sample.txt', 'ud/samples/es_gsd-ud-train-true.txt')

# es_ancora = create_sample('ud/es_data/es_ancora_ud_train.txt', 'ud/samples/es_ancora_ud_train_sample.txt')
#
# pt_gsd = create_sample('ud/pt_data/pt_gsd_ud_train.txt', 'ud/samples/pt_gsd_ud_train_sample.txt')
# pt_bosque = create_sample('ud/pt_data/pt_bosque_ud_train.txt', 'ud/samples/pt_bosque_ud_train_sample.txt')

#%%

def get_label_column(infile):
    with open(infile) as file:
        labels = [line.split('\t')[-1].rstrip() for line in file.readlines()]
    return labels


#%%

y_true = get_label_column(es_gsd[2])
y_pred = get_label_column(es_gsd[2]) # todo put actual predictions [1]

# print(y_true)
# print(y_pred)
print(cohen_kappa_score(y_true, y_pred))

# >>> from sklearn.metrics import confusion_matrix
# >>> y_true = [2, 0, 2, 2, 0, 1]
# >>> y_pred = [0, 0, 2, 2, 0, 2]
# >>> confusion_matrix(y_true, y_pred)
# array([[2, 0, 0],
#        [0, 0, 1],
#        [1, 0, 2]])