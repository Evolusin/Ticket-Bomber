import requests
import base64

url = 'https://hd.infocomp.pl/api/Authorization'
url2 = 'https://hd.infocomp.pl/api/ticket'
params = {
    'categoryId':36,
    'body':'sample',
    'subject':'Test API',
    'priorityId':0
}


loginy = {
    'username': 'bartlomiej.bruzdowski@infocomp.pl',
  'password':'Tomisław-apoloniusz-curus-bachleda-farrell1'}

# def autoryzacja:
#     connector = requests.post(url, headers=headers, params=params, cookies=cookies, data=data)
def get_header(data):
    return {
        "Content-Type":"application/json",
        "Authorization": "Basic "
                              + base64.b64encode(
            bytes(
                f'{data["username"]}:{data["password"]}', "utf8"
            )
        ).decode("utf8")
    }
print(get_header(loginy))
connector = requests.post(url2, headers=get_header(loginy), params=params)
print(connector.status_code)
r=connector.text
print(r)