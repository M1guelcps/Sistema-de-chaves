import random
import string
import os

def gerar_chave_licenca(tamanho=16):
    caracteres = string.ascii_uppercase + string.digits
    chave = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return chave

# Gerar e armazenar as chaves em arquivos separados
if not os.path.exists('chaves_licenca'):
    os.makedirs('chaves_licenca')

with open('chaves_licenca/todas_as_chaves.txt', 'w') as todas_as_chaves_file:
    for i in range(1000):
        chave = gerar_chave_licenca()
        with open(f'chaves_licenca/chave_{i+1}.txt', 'w') as file:
            file.write(chave)
        todas_as_chaves_file.write(chave + '\n')
