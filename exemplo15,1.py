def voto(nas, nome):
    nas = 2025 - nas
    if nas >= 18:
        print(f'Com {nas}: Voto Obrigatorio')
    elif nas >= 16:
        print(f'Com {nas}: Voto opcioal')
    else:
        print(f'Com {nas}: Voto NEGADO')

nas = int(input('Digite o ano de nascimento: '))
nome = str(input('Digite o nome: '))
voto(nas,nome)
