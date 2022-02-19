import os

import os
import pandas as pd
import re

#%%
directory = "postscriptum_data"
data = []  
for root, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        file_name = (os.path.join(root, file))
        if 'ES' in file_name:
            lang = 'spanish'
        else:
            lang = 'portuguese'
        with open(file_name, 'r') as infile:
            for line in infile:

                match = re.match("se", line) # To many encoding errors; applying filter for grapheme 'se' in separate file
                if match:
                    line_dict = {}
                    line_dict = {'filename': file_name[18:-4],
                                 'lang': lang,
                                 'word': line.split('\t')[0],
                                 'norm': line.split('\t')[1],
                                 'pos': line.split('\t')[2],
                                 'lemma': line.split('\t')[3].strip()}

                    data.append(line_dict)
                    continue
                else:
                    continue

    df = pd.DataFrame(data)
    df_pos = df[ (df['pos'] != '') & (df['lemma'] != '')]
    df_pos.to_csv('postcriptum_se.txt', index=False)
#%%
# get stats
    total = len(df)
    df_PCOCNOOO = df[(df.pos == str('PC0CN000'))]
    df_PC3CN000 = df[(df.pos == str('PC3CN000'))]
    df_NP00000 = df[(df.pos == str('NP00000'))]

    df_stats = pd.DataFrame({'n': [len(df_PCOCNOOO), len(df_PC3CN000), len(df_NP00000), total],
                             'tags': ['PC0CN000', 'PC3CN000', 'NP00000','total']}).set_index('tags')

    with open('coser_stats.txt', 'a') as outfile:
        outfile.write(df_stats.to_string())















