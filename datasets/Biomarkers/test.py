import json
import requests
from pprint import pprint
import csv
import pandas as pd

url = 'https://www.vmh.life//_api/biomarkers/'
number_pages = 1
for i in range(1, number_pages+1):
    response = requests.request("GET", f'https://www.vmh.life//_api/biomarkers/?page={i}')
    response = response.json()

    if i == 1:
        reactions = pd.DataFrame(response["results"])
    else:
        biomarkers_to_add = pd.DataFrame(response["results"])
        biomarkers = pd.concat([biomarkers, biomarkers_to_add])
        if i == '3':
            break

for metabolites in response['results']:
    name_ofdw = metabolites['iem']['name']
    type_ofd = metabolites['iem']['dtype']
    notes_ofd = metabolites['iem']['notes']
    phenotype = metabolites['iem']['phenotype']
    organ_affected = metabolites['iem']['organ']
    cheBlId_ofm = metabolites['metabolite']['cheBlId']
    description_ofm = metabolites['metabolite']['description']
    fullName_ofm = metabolites['metabolite']['fullName']
    inchiKey_ofm = metabolites['metabolite']['inchiKey']
    inchiString_ofm = metabolites['metabolite']['inchiString']
    keggId_ofm = metabolites['metabolite']['keggId']
    casRegistry_ofm = metabolites['metabolite']['casRegistry']
    value_ofm = metabolites['value']
    normal_conc_ofm = metabolites['normalConcentration']
    ramedis_ofm = metabolites['ramedis']
    range_conc_ofm = metabolites['rangeConcentration']
    print(value_ofm)

