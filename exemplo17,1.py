def leiaint(n):
    while True:
        valor = input(n)
        if valor.isnumeric():
            return int(valor)
        else:
            print('Error, tente novamente!')

def leiafloat (v):
    while True:
        value = input(v)
        if value.isnumeric():
            return float(value)
        else:
            print('Error, Tente novamente!!')

i = leiaint('Digite um numero inteiro: ')
f = leiafloat('Digite um numero flutuante: ')
print(f'Numero inteiro foi {i} e numero real foi {f}')