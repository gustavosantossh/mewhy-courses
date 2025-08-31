arquivo = "data.csv"
with open(arquivo) as open_file:
    lines = open_file.readlines()
    
# for l in lines:
#     print(l)

dados = dict()

chaves = lines[0].strip().split(";")

for c in chaves:
    dados[c] = []

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])
        
# print(dados)
        
idades = []

for m in dados["idade"]:
    idades.append(int(m))
    
media = sum(idades) / len(idades)
    
print(media)
# for a in range(0,100):
#     print(a)