import os
import time
import pandas as pd
from urllib.request import urlopen, Request

os.chdir('/Users/name/downloads/logos_folder')
df = pd.read_csv("~/downloads/logos.csv")

#df2 = df[(df['Found']==0)].reset_index()

#df['cname'] = df[['name']].replace(' ', '_', regex=True)

def download_img(img_url, img_name):
    request = Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
    response = urlopen(request)
    with open(img_name, "wb") as f:
       f.write(response.read())

for i in range(len(df['logo_url'])):
    try:
        download_img(df['logo_url'][i],df['cname'][i]+'.png')
        #print(df['id'][i])
    except:
        print(df['logo_url'][i])
    time.sleep(1)
