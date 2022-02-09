import zipfile
with zipfile.ZipFile('file.zip', 'r') as zip_ref:
    zip_ref.extractall('temp')