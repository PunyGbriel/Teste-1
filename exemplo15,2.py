import math
def fatorial(v, show=0):
    calculo = 1
    if show == True:
        print(f'{v}! = ', end='')
        for i in range(v):
            calculo = v * i
            print(f' {i} X', end='')
        print('= ',calculo)
    else:
        for i in range(v):
            calculo = v * i
        print(calculo)
fatorial(4, True)