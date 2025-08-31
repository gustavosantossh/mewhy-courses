txt = "Meu texto de exemplo para escrita."

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, 'a') as open_file:
    open_file.write(txt + "\n")