#Request module
import requests
r = requests.get("https://site.financialmodelingprep.com/")
print(r.text)