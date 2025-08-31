dados = {
    'nome': 'Gustavo',
    'sobrenome': 'Henrique',
    'idade': 21
}

print('Items do objeto: ', dados.items())

for i, j in dados.items():
    print('Dentro do for: ', i, j)

A, B, C = 'a', 'b', 'c'

print(A, B, C)

# Pega os 3 primeiros
D, E, F, *resto = 'D', 'E', 'F', 'G', 'H', 'I'

print(D, E, F, resto)

# Pega os 3 ultimos
*resto, D, E, F = 'D', 'E', 'F', 'G', 'H', 'I'

print(D, E, F, resto)

# Pega o primeiro e o ultimo
D, *resto, F = 'D', 'E', 'F', 'G', 'H', 'I'

print(D, F, resto)


def soma(a, *args):
    return a + sum(args)

print(soma(1, 10, 20))


def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]
print(soma_quatro(*values))
print(soma(*values))
