import requests
import base64

from requests.auth import HTTPBasicAuth
url = 'https://hd.infocomp.pl/'
res = requests.post(url)
payload = 'POST https://hd.infocomp.pl/api/Authorization'
# login = 'bartlomiej.bruzdowski@infocomp.pl'
# haslo = 'Arcadias123!'
passy = {'bartlomiej.bruzdowski@infocomp.pl':'Arcadias123!'}
usrPass = 'bartlomiej.bruzdowski@infocomp.pl:Arcadias123!'
data_bytes = usrPass.encode("utf-8")
b64Val = base64.b64encode(data_bytes)
print(str(b64Val))

g=requests.post(url,
                headers={"Authorization": "Basic "+ str(b64Val)},data = payload)

print(g)