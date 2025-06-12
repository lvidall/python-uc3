# def criar_arquivo(nome_arquivo: str, conteudo: str):
#     """Cria um arquivo com nome e conteudo fornecidos."""
#     with open(nome_arquivo, 'w') as arquivo:
#         arquivo.write(conteudo)
#         print('arquivo criado com suceso')



# nome = input('Digite o nome do arquivo: ')
# criar_arquivo(f'./Aula05/arquivos/{nome}.txt', 'Este é um exemplo de arquivo criado com python' )

# def ler_arquivo(nome_arquivo: str):
#     """retrna um conteudo de arquivo"""
#     with open(nome_arquivo, 'r') as arquivo:
#         return arquivo.read()



# nome = input('Digite o nome do arquivo: ')
# print(ler_arquivo(f'./Aula05/arquivos/{nome}.txt' ))


# def adicionar_conteudo(nome_arquivo: str, conteudo: str):
#     """Adicionar um conteúdo ao final de arquivo: """
#     with open(nome_arquivo, 'a') as arquivo:
#         arquivo.write('\n' + conteudo)
#         print('Conteudo adicionadocom sucesso')


#Remover arquivo
# import os

# def remover_arquivo(nome_arquivo: str):
#     """Exclui o arquivo se existir"""
#     if os.path.exists(nome_arquivo):
#         os.remove(nome_arquivo)
#         print('Arquivo removido com secesso')
#     else:
#         print('Arquivo não encontrao')

# remover_arquivo(f'./Aula05/arquivos/{nome}.txt')

#Contar linhas de um arquivo

# def contar_linha(nome_arquivo: str) -> int:
#     """Retornar a quantidade de linha de um arquivo."""
#     with open(nome_arquivo, 'r') as arquivo:
#         return len(arquivo.readlines())

# nome = input('Digite o nome do arquivo: ')
# print(Contar_linha(f'./Aula05/arquivos/{nome}.txt'))

def verificar_palavra(nome_arquivo: str, palavra: str ) -> bool:
     """Retornar a verificação de uma palavra dentro de um arquivo."""
     with open(nome_arquivo, 'r') as arquivo:
      return palavra in arquivo.read()
nome = input('Digite o nome do arquivo: ')
print(verificar_palavra(f'./Aula05/arquivos/{nome}.txt', 'python-uc3'))


