import os
import requests


api_address = os.environ.get("APP_URL")

# requête
r = requests.post(
    url=f'{api_address}/permissions',
    auth = ('alice','wonderland')
)

r1 = requests.post(
    url=f'{api_address}/permissions',
    auth = ('bob','builder')
)


r2 = requests.post(
    url=f'{api_address}/permissions',
    auth = ('clementine','mandarine')
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''
output1 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code1}

==>  {test_status1}

'''

output2 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="clementine"
| password="mandarine"

expected result = 200
actual result = {status_code2}

==>  {test_status2}
==>  {status_code2}

'''




# statut de la requête
status_code = r.status_code
status_code1 = r1.status_code
status_code2 = r2.status_code


# affichage des résultats d'alice
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))


# affichage des résultats d'bob
if status_code1 == 200:
    test_status1 = 'SUCCESS'
else:
    test_status1 = 'FAILURE'
print(output1.format(status_code1=status_code1, test_status1=test_status1))


# affichage des résultats clementine
if status_code2 == 200:
    test_status2 = 'SUCCESS'
else:
    test_status2 = 'FAILURE'
print(output2.format(status_code2=status_code2, test_status2=test_status2))


# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output1)

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output2)