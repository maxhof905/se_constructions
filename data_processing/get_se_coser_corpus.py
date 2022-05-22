# maxhof905

# gather se in coser

import os
import pandas as pd
from bs4 import BeautifulSoup

#%%

directory = "COSER-2.0-XML"
corpus_list = []
for root, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        file_name = (os.path.join(root, file))
        with open(file_name, 'r') as infile:
            soup = BeautifulSoup(infile, features="html.parser")
            se_list = soup.find_all(lemma="se")
            for word in se_list:
                data = {'filename': file_name,
                        'province': soup.provincia.text.strip(),
                        'enclave': soup.enclave.text.strip(),
                        'id': word.get('id'),
                        'word': word.text,
                        'pos': word.get('pos'),
                        'lemma': word.get('lemma')}
                corpus_list.append(data)
df = pd.DataFrame(corpus_list)
df.to_csv('coser_se.txt', index=False)

