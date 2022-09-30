import json

import requests
from pprint import pprint
import csv

url = 'https://www.vmh.life//_api/biomarkers/'
url_2 = 'http://www.vmh.life/_api/biomarkers/?page=2'
url_3 = 'http://www.vmh.life/_api/biomarkers/?page=3'
response = requests.get(url).json()
pprint(response)
for i in range(1, number_pages+1):
    response = requests.request("GET", f'https://www.vmh.life//_api/biomarkers/?page={i}')
    response = response.json()

    if i == 1:
        reactions = pd.DataFrame(response["results"])
    else:
        biomarkers_to_add = pd.DataFrame(response["results"])
        biomarkers = pd.concat([biomarkers, biomarkers_to_add])

name_ofdw = response['results'][0]['iem']['name']
type_ofd = response['results'][0]['iem']['dtype']
notes_ofd = response['results'][0]['iem']['notes']
phenotype = response['results'][0]['iem']['phenotype']
organ_affected = response['results'][0]['iem']['organ']
cheBlId_ofm = response['results'][0]['metabolite']['cheBlId']
description_ofm = response['results'][0]['metabolite']['description']
fullName_ofm = response['results'][0]['metabolite']['fullName']
inchiKey_ofm = response['results'][0]['metabolite']['inchiKey']
inchiString_ofm = response['results'][0]['metabolite']['inchiString']
keggId_ofm = response['results'][0]['metabolite']['keggId']
casRegistry_ofm = response['results'][0]['metabolite']['casRegistry']
value_ofm = response['results'][0]['value']
value_ofm = response['results'][0]['normalConcentration']
value_ofm = response['results'][0]['ramedis']
value_ofm = response['results'][0]['rangeConcentration']








""" Question: I don't know how to pull the data from all the pages"""









