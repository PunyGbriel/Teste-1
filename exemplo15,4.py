def leiaint(stri, v=0):
    while True:
        valo = input(stri)
        if valo.isnumeric():
            return int(valo)
        else:
            print('Error')


n = leiaint('Digite algo: ')
print('Voce Digitou: ', n)