import json

import requests
from pprint import pprint
import csv

url = 'https://www.vmh.life//_api/biomarkers/'
url_2 = 'http://www.vmh.life/_api/biomarkers/?page=2'
url_3 = 'http://www.vmh.life/_api/biomarkers/?page=3'

response = requests.get(url_3).json()

pprint(response)


""" Question: I don't know how to pull the data from all the pages"""









