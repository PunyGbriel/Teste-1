import time
def contador(i, f, p):
    """
    c = recebe i = inicio, para funcionar como um contador
    f = final
    p = passo
    Na linha do while, se o inicio for menor doq o final
    ele vai fazer uma contagem regressiva do numero que foi inserido
    logo com o if, ele fara o uma contagem ao contrario.
    """
    c = i
    while c <= f:
        print(f'{c}...', end='')
        c += p
        time.sleep(0.5)
    if c > f:
        for a in range(i, f - 1, -abs(p)):
            print(f'{a}...', end='')
            time.sleep(0.5)
help(contador)