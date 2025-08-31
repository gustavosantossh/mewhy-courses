# Adicionando elementos em lista com for

# Modo normal
x = []
for i in range(1,101):
    x.append(i)
    
print(x)

print('-----------------------------------------------------------------')
    
# List comprehension

y = [i for i in range(0, 110, 10)]

print(y)

print('-----------------------------------------------------------------')

# List comprehension com condicional

def eh_par(x):
    return x % 2 == 0

w = [i for i in range(1,101) if eh_par(i)]

print('Lista par: ', w)