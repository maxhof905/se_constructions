import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%
def get_class_dist(df_col):
    """
    plot label distribution
    """
    data = df_col.value_counts(normalize=True).rename('percentage').mul(100).reset_index().rename(columns = {"index":"label"})
    sns.set(font="Times New Roman", font_scale=2)
    plot = sns.barplot(x="label", y="percentage", data=data, palette="binary")
    plot.set_xticklabels(plot.get_xticklabels(),
                          rotation=45,
                          horizontalalignment='right',
                         weight='bold')

#%%
# train_path = '/Users/Maxine/Desktop/se_corpus/ud/pt_data/pt_bosque-ud-train.txt'
# test_path = '/Users/Maxine/Desktop/se_corpus/ud/pt_data/pt_bosque-ud-test.txt'
# dev_path = '/Users/Maxine/Desktop/se_corpus/ud/pt_data/pt_bosque-ud-dev.txt'

train_path = '/Users/Maxine/Desktop/se_corpus/ud/es_data/es_ancora-ud-train.txt'
test_path = '/Users/Maxine/Desktop/se_corpus/ud/es_data/es_ancora-ud-test.txt'
dev_path = '/Users/Maxine/Desktop/se_corpus/ud/es_data/es_gsd-ud-dev.txt'

train = pd.read_csv(train_path, sep='\t', names=['text', 'tokenized_text', 'se_label'])
train.drop(columns=['text'], inplace = True)
dev = pd.read_csv(dev_path, sep='\t', names=['text', 'tokenized_text', 'se_label']) # colab
dev.drop(columns=['text'], inplace = True)
test = pd.read_csv(test_path, sep='\t', names=['text', 'tokenized_text', 'se_label']) # colab
test.drop(columns=['text'], inplace = True)

se_corpus = pd.concat([train, dev, test]) # because the data was fileted for 'se' the data splits are not reliable anymore

#%%
get_class_dist(se_corpus.se_label)

#%%
# eventually save the plots
plt.savefig('es_labels.png', bbox_inches='tight')
plt.tight_layout()
plt.show()