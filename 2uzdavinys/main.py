import json  # pajungem moduli darbui su failais json
from pprint import pprint  # pajungem Pprint kad graziau isvestu i ekrana tekstas(duomenis)
with open('personal.json', 'r', encoding='utf-8') as f:  # atidarem faila su duomenemis
    text = json.load(f)  # kas gavosi viska sustumem i text kintamaji
    pprint(text)  # isprintinom i ekrana
for txt in text['personal']:  # sukuriam cikla,kuris iteruoja kiekviena eilute
    print(txt['name'], ':', txt['salary'])  # ir viska printinam, kas yra name ir salary raktuose
    
#output
{'personal': [{'name': 'Вася', 'salary': 5000},
              {'name': 'Саша', 'salary': 6000},
              {'name': 'Петя', 'salary': 9000},
              {'name': 'Даша', 'salary': 10000},
              {'name': 'Маша', 'salary': 11000}]}
Вася : 5000
Саша : 6000
Петя : 9000
Даша : 10000
Маша : 11000

Process finished with exit code 0
