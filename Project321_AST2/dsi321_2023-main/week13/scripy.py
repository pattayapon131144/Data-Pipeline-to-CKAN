import pandas as pd
import requests
import json, os
from datetime import datetime

## create package
def sendMetaToCkan(url_ckan, api_key, ckan_meta):
    headers = {
        'content-type': 'application/json',
        'Authorization': api_key,
    }

    url = '{}/api/action/package_create'.format(url_ckan)
    respond = requests.post(url, data=json.dumps(ckan_meta), headers=headers)
    res_text = respond.content.decode('utf-8').replace('\n','br')
    print(res_text)
    
## Upload File
def uploadFileToCkan(url_ckan, api_key, file_meta, path_input):
    headers = {'X-CKAN-API-Key': api_key}
    url = '{}/api/action/resource_create'.format(url_ckan)
    with open(path_input, "rb") as f:
        form_file = {'upload': f}
        respond = requests.post(url, data=file_meta, headers=headers, files=form_file)
        res_text = respond.content.decode('utf-8').replace('\n','br')
        print(res_text)
        print('<b>File has been uploaded</b>')

dfs = pd.read_html("https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false", header=1)
df=dfs[0]
df.drop(['1'], axis =1)
df.to_csv("ast2.csv")

#### import ลง CKAN

with open('metadata.json', encoding='utf-8') as data:
     ckan_meta = json.load(data)


url_ckan = os.getenv("CKAN_URL","https://ckan.data.storemesh.com" )  # ใส่ ip ของ ckan server ตรงนี้
api_key = os.getenv("TOKEN","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODA0OTg0NTAsImp0aSI6InBIeE5MbTFGVUpPTFQ1Mm9ad20zaGpQblFIV0JmNUtISWM5ck1rQk1GZ1FVakpUaktJbERfM1dib1NIQU5aYXBobzJCazByTU9MdXlFSUdjIn0.r7WW-76Yb6itT9z2mebvqN-_OVp1JYkx2H0kJVet7QU") 


now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
## for upload file
file_meta = {
    'package_id': ckan_meta['name'],
    'name': f'data-scripy-{now}',
}
# path_input = './result.csv'
path_input = './ast2.csv'
sendMetaToCkan(url_ckan, api_key, ckan_meta)
uploadFileToCkan(url_ckan, api_key, file_meta, path_input)