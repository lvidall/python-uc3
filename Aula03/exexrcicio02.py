import time 

partida = int(input('informe o valor de partida: '))

def contador(partida):
    while partida >= 0:
        print(f'{partida}')
        time.sleep(1)
        partida -= 1
contador(partida)