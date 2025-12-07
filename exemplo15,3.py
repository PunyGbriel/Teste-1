def ficha(nome='', gols=0):
    if nome == '' and gols == '':
        print(f'<DESCONHECIDO> e fez <DESCONHECIDO>')
    elif gols == '':
        print(f'{nome} e fez <DESCONHECIDO>')
    elif nome == '':
        print(f'<DESCONHECIDO> e fez {gols}')
    else:
        print(f'{nome} e {gols} gols')


print('-'*30)
nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input('Digite a Quantidade de gols: ')).strip()
ficha(nome,gols)