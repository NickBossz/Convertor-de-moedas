import json
import requests

def converter(valor, moeda1, moeda2):
    api = requests.get(f"https://economia.awesomeapi.com.br/{moeda1}-{moeda2}/")
    
    if api.status_code == 200:
        jsonArmazenado = api.json()
        return float(jsonArmazenado[0]["bid"]) * valor
    else:
        return None

print("==== Conversor de moedas ====")
print("Lista de algumas moedas:\nBRL\nUSD\nEUR\nJPY\nBTC\nETH\nDOGE")

valor = float(input("Valor: "))
moeda_1 = input("Converter de: (sigla) ")
moeda_2 = input("Converter para: (sigla) ")

valorfinal = converter(valor, moeda_1, moeda_2)

if valorfinal is not None:
    print(f"{valor} {moeda_1} é igual à {valorfinal} {moeda_2}")
else:
    print("Esta moeda não existe!")

input("Pressione enter para sair!")
