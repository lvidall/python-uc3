import time

tabuada = int(input("Digite qual tabuada voce quer: "))
for i in range(0, 11):
    print(f'{i} x {tabuada} = {i*tabuada}')
    time.sleep(1)

calculo(tabuada)    