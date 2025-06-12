def exibir_menu ():
    print("\nMenu:")
    print("1 - Dizer olá")
    print("2 - cadastro")
    print("3 - sair")

interacoes = 0
opcao = 0 

while opcao != 3:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        print("Por favor digite um numero válido.")
        continue
    interacoes  += 1 

    if opcao == 1:
        print("Seja bem vindo")
    elif opcao == 2:
        print("Faça seu cadastro")
    elif opcao == 3:
        print("Sair do programa")
    else:
        print(Opçãoinválida.)

    print(f"\nVocê interagiu com o mennu {interacoes} vez até sair.")