import requests
import zipfile

r = requests.get("path of zip file")
with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data..zip', 'r') as data_zip:
    print(data_zip.namelist())
    print(data_zip.extractall())
    

