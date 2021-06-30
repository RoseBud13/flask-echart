import requests
from requests_ntlm import HttpNtlmAuth
# import re


def getData():
    '''Get data from API

    Methods: using reguests.get() and HttpNtlmAuth to get and auth

    Return: return a bunch of json data with escape character
    '''
    # api_res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    url = 'http://mbase.got.volvocars.net/mbaseCache/api/hash/DSLS_gotsvl1144_Info'
    api_res = requests.get(url, auth = HttpNtlmAuth('bppcswf1', 'volvo123ABC'))
    # print(api_res)
    data_raw = api_res.text
    # print(data_raw)
    # data = re.sub(r'\\','',data_raw)
    # print(type(data_raw))
    return data_raw
