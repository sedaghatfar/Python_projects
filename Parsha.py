import requests
from datetime import date

today = str(date.today().strftime('%m/%d/%Y'))

stem = 'http://db.ou.org/zmanim/getParshaData.php?date='

stems = stem + today
par = requests.get(stems)
data = par.json()

print(data['parsha'])
