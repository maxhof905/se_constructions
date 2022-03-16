import pandas as pd
#%%


def get_se_dict(infile):
    sentences = []
    lines = []
    se_dict = dict()
    new_line = '\n'
    se_sentences = []
    with open(infile) as file:
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
            for elem in sentence:
                if elem.startswith('# text ='):
                    text = elem.strip('# text =').rstrip()
                if 'se\tse' in elem:
                    se_dict[text] = elem.split('\t')[7]
    return se_dict
#%%
filename = 'pt_bosque-ud-train.conllu'
outfile = filename[:-7]+'.txt'
stats_file = filename[:-7]+'_stats.txt'
df = pd.DataFrame.from_dict(get_se_dict(filename), orient='index')
df.to_csv(outfile)
df.value_counts().to_csv(stats_file)

#todo id text tag
#todo eliminate quotation marksa
#%%



