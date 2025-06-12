palavra = input('Digite uma palavra: ')

def verifica_palindromo(palvra):
    if palavra == palavra [::-1]:
        return True
    else:
        return False

print(verfica_palindromo(palvra))