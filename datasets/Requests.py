import json

import requests
from pprint import pprint
import csv as cv

url = 'https://www.vmh.life//_api/biomarkers/'

response = requests.get(url)

data = response.json()
pprint(data)

print(data['results'])
with open('results_page_1.json','w') as f:
   cv.dump(data['results'], f , indent= 2)

   """ Question: I don't know how to pull the data from all the pages"""









