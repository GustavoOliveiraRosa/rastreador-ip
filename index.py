
# Importando library
import requests
from requests.exceptions import HTTPError
import json
import os

os.system("clear")

print("\033[1;32m")
print("============================================")
print("██╗  ██╗██╗███████╗ ██████╗ ██╗  ██╗ █████╗ ")
print("██║  ██║██║██╔════╝██╔═══██╗██║ ██╔╝██╔══██╗")
print("███████║██║███████╗██║   ██║█████╔╝ ███████║")
print("██╔══██║██║╚════██║██║   ██║██╔═██╗ ██╔══██║")
print("██║  ██║██║███████║╚██████╔╝██║  ██╗██║  ██║")
print("╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ - Rastreador IP")
print("============================================")
print("\033[0;0m")


# Capturando KEY de usuário

key = input("\033[1;36mKEY DO IPSTACK=>\033[0;0m ")
ip = input("\033[1;36mIP ALVO =>\033[0;0m ")

os.system("clear")

print("\033[1;32m")
print("============================================")
print("██╗  ██╗██╗███████╗ ██████╗ ██╗  ██╗ █████╗ ")
print("██║  ██║██║██╔════╝██╔═══██╗██║ ██╔╝██╔══██╗")
print("███████║██║███████╗██║   ██║█████╔╝ ███████║")
print("██╔══██║██║╚════██║██║   ██║██╔═██╗ ██╔══██║")
print("██║  ██║██║███████║╚██████╔╝██║  ██╗██║  ██║")
print("╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ - Rastreador IP")
print("============================================")
print("\033[0;0m")

try:
    response = requests.get('http://api.ipstack.com/'+str(ip)+'?access_key='+str(key)+'&format=1')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    #print(jsonResponse)
    print('\033[1;33mIP\033[0;0m: ',jsonResponse['ip'])
    print('\033[1;33mTIPO\033[0;0m: ',jsonResponse['type'])
    print('\033[1;33mNome do continente\033[0;0m: ',jsonResponse['continent_name'])
    print('\033[1;33mCódigo do continente\033[0;0m: ',jsonResponse['continent_code'])
    print('\033[1;33mCódigo do País\033[0;0m: ',jsonResponse['country_code'])
    print('\033[1;33mNome do País\033[0;0m: ',jsonResponse['country_name'])
    print('\033[1;33mCódigo da Região\033[0;0m: ',jsonResponse['region_code'])
    print('\033[1;33mNome da Região\033[0;0m: ',jsonResponse['region_name'])
    print('\033[1;33mCidade\033[0;0m: ',jsonResponse['city'])
    print('\033[1;33mLatitude\033[0;0m : ',jsonResponse['latitude'])
    print('\033[1;33mLongitude\033[0;0m: ',jsonResponse['longitude'])
    print('\n\n\n')

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
