import pandas as pd
import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
people = response.json()['people']

astrolist = []
craftlist = []

for i in people:
    a = i.get('name')
    b = i.get('craft')
    astron = astrolist.append(a)
    crews = craftlist.append(b)
    
astronants = pd.DataFrame(list(zip(craftlist, astrolist)), columns = ['Craft', 'Name'])


print (astronants)
