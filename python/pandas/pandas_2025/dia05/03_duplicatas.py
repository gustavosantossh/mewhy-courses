# %%

import pandas as pd

# %%
dataset = pd.DataFrame({
    "nome": [
        "João", "Maria", "Carlos", "João", "Ana", "Carlos", 
        "Fernanda", "Maria", "Ana", "João"
    ],
    "sobrenome": [
        "Silva", "Oliveira", "Santos", "Silva", "Pereira", "Santos", 
        "Moura", "Oliveira", "Pereira", "Souza"
    ]
})

dataset
# %%

dataset.drop_duplicates(keep='first', subset=['nome', 'sobrenome'])
# %%
