import pandas as pd
import csv
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
            counter = 0
            for elem in sentence:
                if elem.startswith(('# sent_id =')):
                    sent_id = elem.strip('# sent_id =').rstrip()
                if elem.startswith('# text ='):
                    # text = elem.strip('# text =').rstrip().replace(',', '')
                    text = elem.strip('# text =').rstrip().replace('«', '').replace('»', '').replace('-- ', '').replace('(', '').replace(')', '').replace('\'', '')

                if 'se\tse' in elem.lower(): #todo match more precisely: se él cases are lost
                    counter += 1
                    se_tag = elem.split('\t')[7]

            if counter == 1:
                se_dict[sent_id] = [text, se_tag]

    return se_dict
#%%
filename = 'es_ancora-ud-train.conllu'
outfile = filename[:-7]+'.txt'
stats_file = filename[:-7]+'_stats.txt'
df = pd.DataFrame.from_dict(get_se_dict(filename), orient='index')
print(df.shape)
# # df.index.rename('sent_id', inplace=True)
# # df = df[['sent_id', 'sent', 'tag']]
# # df.to_csv(outfile, header=False, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
# df.to_csv(outfile, header=False, sep='\t')
# df.value_counts().to_csv(stats_file)

#todo eliminate sentences that contain se twice
#%%



