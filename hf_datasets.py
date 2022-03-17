
import numpy
import transformers
import datasets
from datasets import load_dataset
import requests
#%%
url = "https://raw.githubusercontent.com/UniversalDependencies/UD_Spanish-AnCora/master/es_ancora-ud-dev.conllu"
filename = 'ud/es_dev.txt'
r = requests.get(url)

f = open(filename,'w')
f.write(str(r.content))
#%%