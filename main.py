import requests
import base64


url = 'https://hd.infocomp.pl/api/Authorization'
url2 = 'https://hd.infocomp.pl/api/ticket'
url3 = 'https://hd.infocomp.pl/api/UpdateTicket'
list_tickets = []
usr_load = 'test'
usr_load = 'str'
passwd_load = 1
tytul = 1

def t_tresc():
    global tytul
    print("Wprowadź tytuł ticketu")
    tytul = input()


def login():
    file = open('login.txt','r',encoding='utf-8')
    line = file.readlines()
    global usr_load
    global passwd_load
    usr_load = line[0].rstrip("\n")
    passwd_load = line[1]

t_tresc()
login()
loginy = {
    'username': usr_load,
  'password':passwd_load}
params = {
    'categoryId':36,
    'body':'jw',
    'subject':tytul,
    'priorityId':0
}
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

def close_ticket(url,params):
    connector = requests.post(url, headers=get_header(loginy), params=params)
    print(connector.status_code)
    t = connector.text


send_ticket(url2,params)
list_tickets = list(map(int,list_tickets))
# print(list_tickets)

for i in range(len(list_tickets)):
    params2={
        'id':list_tickets[i],
        'statusId':3,
        'assignedUserId':734
    }
    # print(params2)
    close_ticket(url3,params2)