# dsi321_2023 #asa2
# Setting Up
* Create requirement.txt, tell dependencies you need (docker file will read this file later)
```
pandas
requests
lxml
html5lib
beautifulsoup4
```
* Install dependencies for Jupyter
```bash
pip install -r requirement.txt 
```
* Create Dockerfile
```Dockerfile
FROM python:3.8
WORKDIR /code
COPY . .
COPY requirement.txt  requirement.txt
RUN pip install -r /code/requirement.txt
# เหมือนจะขาดไปหนึ่งบรรทัด
```

* Create conjob.yaml (see details in the following link)

Please change the "name" to your team_id 
https://github.com/wasit7/dsi321_2023/blob/main/week13/conjob.yaml
```yml
name: scripy-web-wsl01 # change team-id to your team e.g. wsl01

```
* Modify schedule cronjob to every 6 hours
* Warning : this step requires publish your docker image to docker hub 
```yaml
schedule: "* * * * *"   # modify to every 6 hours
image: kran13200/simple-scripy:latest # use your docker hub
```
* Create metadata.json  (see detail in link) : you have to modified information corresponding to your information - warning : name should be unique small letter and title should be big letter  
https://github.com/wasit7/dsi321_2023/blob/main/week13/metadata.json
* Edit dataset name and title to match your dataset and contain your team_id
```json
    "name": "thailand_gdp03",   # must change this line to weather_wsl01
    "title": "THAILAND_GDP_03", # must change this line to weather_wsl01
```

# Data Source
* Weather Data Source : https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false
* Pandas can load HTML table tag with single function
```python
# from URL
dfs = pd.read_html("https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false")
# from .env : WEB_SCRIPY MUST PRE-DEFINE IN .env
import os
dfs = pd.read_html(os.getenv("WEB_SCRIPY"))
```


# Data Preparation and Metadata
* Before write python code in script that send to deploy in real server, you must test and confirm your code in Jupyter.
* Copy .env-template to .env
```bash
cp .env-template .env      #ubuntu / mac
copy .env-template .env    #window
```

* Specify TOKEN (permission to access ckan, see in code week 12), CKAN_URL, WEB_SCRIPY URL in .env

```bash
TOKEN=xxxxxxxxxxx   # ใส่ TOKEN
CKAN_URL=https://ckan.data.storemesh.com
WEB_SCRIPY=yyyyyyyyy # ใส่ URL web สำหรับ scrap 
```
* Create your new Jupyter notebook file 
* Load data source from google sheet link above
* Use pandas to ETL data and transform into appropriate structure and export to df.CSV

# Send Data to CKAN Dataset

* This set step require metadata.json and function to send 

## Create dataset only one time
* You may create dataset in Jupyter with code like week 12 

## Upload data
* See detail in scripy.py

# Publish to Docker hub
* You must have docker hub account
* Try to publish your image to docker hub
* in .yaml file use your image instead

# Kubernates CronJob
* modified cronjob in metadata.json at schedule
* deploy to kubernetes server see detail in week 9

# Data Visualization and Interpretation
* use you favorite tool to create a meaningful table or chart. Then use it in report to tell thesory and facts those you have discovered.

# Project References
* https://www.iqair.com/th/air-pollution-data-api
* [Air Quality Index (AQI)](https://en.wikipedia.org/wiki/Air_quality_index)
* [API Reference](https://api-docs.iqair.com/)
* [Crontab Editor](https://crontab.guru/#*_*/6_*_*_*)
* [Weather Data Source](https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false)
