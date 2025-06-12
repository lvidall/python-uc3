def soma_numeros(nome_arquivo: str) -> int:
    """Retorna a dos numeros de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo: 
        return sum(int(linha.strip())for linha in arquivo)

nome = input('Digite o nome do arquivo: ')
criar_arquivo(f'./Aula05/arquivos/{nome}.txt', 'Este é um exemplo de arquivo criado com python' )       