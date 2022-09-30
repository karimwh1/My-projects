import requests
from pprint import pprint
import pandas  as pd
url = 'https://www.vmh.life//_api/biomarkers/'
url_2 = 'http://www.vmh.life/_api/biomarkers/?page=2'
url_3 = 'http://www.vmh.life/_api/biomarkers/?page=3'
responce = requests.get(url_3).json()
df = pd.json_normalize(responce['results'])
df.to_csv('results_3.csv', index = False)

print(df)