import requests
import base64

url = 'https://hd.infocomp.pl/api/Authorization'
url2 = 'https://hd.infocomp.pl/api/ticket'
url3 = 'https://hd.infocomp.pl/api/UpdateTicket'
params = {
    'categoryId':36,
    'body':'sample',
    'subject':'Test API',
    'priorityId':0
}
# params2 = {
#     'id':113982,
#     'statusId':3
# }
list_tickets = []

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

#send ticket
def send_ticket(url,params):
    connector = requests.post(url, headers=get_header(loginy), params=params)
    print(connector.status_code)
    r=connector.text
    list_tickets.append(r)


send_ticket(url2,params)
list_tickets = list(map(int,list_tickets))
print(list_tickets)



def close_ticket(url,params):
    connector = requests.post(url, headers=get_header(loginy), params=params)
    print(connector.status_code)
    t = connector.text

for i in range(len(list_tickets)):
    params2={
        'id':list_tickets[i],
        'statusId':3,
        'assignedUserId':734
    }
    print(params2)
    close_ticket(url3,params2)