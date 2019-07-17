import requests


#!  Checkout this guys repo : https://github.com/email-verifier/verifier-py

def verify(email, access_token):
    params = (
        ('token', access_token),
    )

    response = requests.get('https://verifier.meetchopra.com/verify/' + email, params=params)

    try:
        data = response.json()
    except:
        return False

    return data['status']

def verifyRequest(email, access_token):
    params = (
        ('token', access_token),
    )
    
    response = requests.get('https://verifier.meetchopra.com/verify/'+ email, params=params)

    try:
        data = response.json()
    except:
        return False

    return data
