import pandas as pd
import os
import glob

os.chdir('/Users/sedaghatfar/downloads/')

path = '/Users/sedaghatfar/downloads/'

allFiles = glob.glob(path + "/*.csv")

frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)

df2 = pd.concat(map(pd.read_csv, allFiles))

print df2.shape

df2 = df2.sort_values(by=['id'])

df2.drop_duplicates()

df2.to_csv('new.csv')
