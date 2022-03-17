import numpy
import pandas
import xlrd

#%%
# excel: guardar como csv > bbedit:abrir y guardar con utf-8 y mac linebreaks
with open('/SE_Carlota/tabla_se.csv', 'r') as infile:
    df = pandas.read_csv(infile, encoding='latin-1')

#%%
    df.head()
#%%
    df = df.drop(['Unnamed: 23', 'Unnamed: 24',
       'Unnamed: 25', 'Unnamed: 26'], axis=1)
#%%
    print(len(df))
    print(df.tail())
    # %%