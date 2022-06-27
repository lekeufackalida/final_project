import os
import requests


api_address = os.environ.get("APP_URL")


url1=f'{api_address}'

r1 = requests.get(url1)

dat = {
        'seniorcitizen' : "Yes",
        'dependents' : "Yes",
        'tenure' : 8.00,
        'phoneservice' : "Yes",
        'mutliplelines' : "No",
        'internetservice' : "Yes",
        'onlinesecurity' : "Yes",
        'onlinebackup' : "No",
        'techsupport' : "Yes",
        'streamingtv' : "No",
        'streamingmovies' : "No",
        'contract' : "one year",
        'paperlessbilling' : "Yes",
        'PaymentMethod' : "Mailed check",
        'monthlycharges' : 30.00,
        'totalcharges' : 400.00  
    }

r2 = requests.post(
    url=f'{api_address}/predict/v1',
    auth = ('bob','builder'),
    json= dat 
)


r3 = requests.post(
    url=f'{api_address}/predict/v2',
    auth = ('alice','wonderland'),
    json= dat 
)

r4 = requests.post(
    url=f'{api_address}/performance',
    auth = ('alice','wonderland'),
    json = {"model":"v1" }
)

l1 = r2.json()
l2 = r3.json()
l3 = r4.json()



output = '''
============================
    Status test
============================

request done at "/status"

expected result = 200
actual result = {status_code}
{o1}
le deuxième
{​p2}

==>  {test_status}

'''
output1 = '''
============================
    Welcome test
============================

request done at "/"

expected result = 200
actual result = {status_code1}

==>  {test_status1}

'''

output2 = '''
============================
    Predict test
============================

request done at "/predict/v1"
| username="bob"
| password="builder"
| seniorcitizen="Yes"
| dependents="Yes"
| tenure=8.00
| phoneservice="Yes"
| mutliplelines="No"
| internetservice="Yes"
| onlinesecurity="Yes"
| onlinebackup="No"
| techsupport="Yes"
| streamingtv="No"
| streamingmovies= "No"
| contract ="one year"
| paperlessbilling="Yes"
| PaymentMethod= "Mailed check"
| monthlycharges= 30.00
| totalcharges=400.00  

expected result = 200
actual result = {status_code2}

==>  {test_status2}
==>  {status_code2}

{l1}

'''


output3 = '''
============================
    Predict test
============================

request done at "/predict/v2"
| username="bob"
| password="builder"
| seniorcitizen="Yes"
| dependents="Yes"
| tenure=8.00
| phoneservice="Yes"
| mutliplelines="No"
| internetservice="Yes"
| onlinesecurity="Yes"
| onlinebackup="No"
| techsupport="Yes"
| streamingtv="No"
| streamingmovies= "No"
| contract ="one year"
| paperlessbilling="Yes"
| PaymentMethod= "Mailed check"
| monthlycharges= 30.00
| totalcharges=400.00  

expected result = 200
actual result = {status_code3}

==>  {test_status3}
==>  {status_code3}

{l2}

'''


output4 = '''
============================
    Performance test
============================

request done at "/performance"
| username="alice
| password="wonderland"

expected result = 200
actual result = {status_code4}

==>  {test_status4}
==>  {status_code4}

{l3}

'''

# statut de la requête

status_code1 = r1.status_code
status_code2 = r2.status_code
status_code3 = r3.status_code
status_code4 = r4.status_code



# affichage des résultats d'alice
if status_code3 == 200:
    test_status3 = 'SUCCESS'
else:
    test_status3 = 'FAILURE'
print(output3.format(status_code3=status_code3, test_status3=test_status3, l2=l2))


#affichage des résultats d'alice
if status_code4 == 200:
    test_status4 = 'SUCCESS'
else:
    test_status4 = 'FAILURE'
print(output4.format(status_code4=status_code4, test_status4=test_status4, l3=l3))



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
print(output2.format(status_code2=status_code2, test_status2=test_status2, l1=l1))


# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output3)

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output1)

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output2)