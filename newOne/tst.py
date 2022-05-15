import requests
BASE_URL='http://127.0.0.1.8000/'
ENDPOINT = 'jsonResponseurl'
res = requests.get(BASE_URL+ENDPOINT)
dta= res.json()
#for x in dta:
#    print('vkey'+x.getValue() )
print(dta['id'])
#print(dta['name'])
