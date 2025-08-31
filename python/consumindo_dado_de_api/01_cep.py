import requests
import json
from tqdm import tqdm
import pandas as pd

# Lista com 10 CEPs válidos
ceps = [
    "01001-000",  # São Paulo - SP
    "01310-200",  # São Paulo - SP
    "20040-020",  # Rio de Janeiro - RJ
    "30130-010",  # Belo Horizonte - MG
    "40010-000",  # Salvador - BA
    "50010-000",  # Recife - PE
    "60020-010",  # Fortaleza - CE
    "70040-010",  # Brasília - DF
    "80010-010",  # Curitiba - PR
    "90010-010"   # Porto Alegre - RS
]

url = "https://viacep.com.br/ws/{cep}/json/" # Placeholder

dados = [] # Lista vazia para armazenar os dados obtidos 

for i in tqdm(ceps):
    response = requests.get(url.format(cep=i)) # url.format(cep=i) -> Pega a string e substitui o valor de {cep} para o valor i. onde i é cep atual dentro da lista de ceps
    
    if response.status_code == 200: 
        dados.append(response.json()) # -> Transforma os dados para um json e salva na lista.  


dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

print(dataset)

with open("ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

# dados = response.text -> Returns a Str Object
# dados = response.json() -> Returns a Json / dict Class/Object

