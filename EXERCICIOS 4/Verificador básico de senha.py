def verificar_senha():
    senha = input("Digite a senha: ")

    tem_numero = any(char.isdigit() for char in senha)
    tem_tamanho = len(senha) >= 8

    if tem_tamanho and tem_numero:
        print("Senha válida.")
    else:
        print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")

verificar_senha()
