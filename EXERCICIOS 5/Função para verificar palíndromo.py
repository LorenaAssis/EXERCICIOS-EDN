def eh_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

frase = input("Digite uma palavra ou frase para verificar se é palíndromo: ")
resultado = eh_palindromo(frase)
print(resultado)
