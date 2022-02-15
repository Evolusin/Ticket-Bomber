import requests
import base64


url = 'https://hd.infocomp.pl/api/Authorization'
url2 = 'https://hd.infocomp.pl/api/ticket'
url3 = 'https://hd.infocomp.pl/api/UpdateTicket'
list_tickets = []
usr_load = None
passwd_load = None
tytul = []
user = None
category = None
contain = None

def t_tresc():
    global tytul
    print("Wczytywanie ticketów")
    file = open('tickety.txt', 'r', encoding='utf-8')
    line = file.readlines()
    for i in range(len(line)):
        tytul.append(line[i].rstrip("\n"))

def login():
    file = open('login.ini','r',encoding='utf-8')
    line = file.readlines()
    file2 = open('config.ini', 'r', encoding='utf-8')
    line2 = file2.readlines()
    global usr_load
    global passwd_load
    global user
    global category
    global contain
    usr_load = line[0].rstrip("\n")
    passwd_load = line[1]
    user = line2[1].rstrip("\n")
    category = line2[3].rstrip("\n")
    contain = line2[5].rstrip("\n")

#zczytanie ticketow
t_tresc()
#zczytanie loginu i hasla z pliku
login()

loginy = {
    'username': usr_load,
  'password':passwd_load}

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
#debug - czy wygenerowane szyforwanie
# print(get_header(loginy))

#send ticket
def send_ticket(url,params):
    connector = requests.post(url, headers=get_header(loginy), params=params)
    #debug - status zwrotny
    # print(connector.status_code)
    r=connector.text
    list_tickets.append(r)

def close_ticket(url,params):
    connector = requests.post(url, headers=get_header(loginy), params=params)
    #debug - status zwrotny
    # print(connector.status_code)
    t = connector.text


# send tickets loaded from list tytul
for i in range(len(tytul)):
    params = {
        'categoryId': category,
        'body': contain,
        'subject': tytul[i],
        'priorityId': 0
    }
    send_ticket(url2,params)

try:
    list_tickets = list(map(int,list_tickets))
except ValueError:
    print("ERROR!")
    print("Upewnij sie czy plik login.txt zawiera poprawny login i haslo do HD")
#debug - lista ticketow
# print(list_tickets)

#assign to user and close tickets from list
for i in range(len(list_tickets)):
    params2={
        'id':list_tickets[i],
        'statusId':3,
        'assignedUserId':user
    }
    close_ticket(url3,params2)