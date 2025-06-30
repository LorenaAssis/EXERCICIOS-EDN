def classificar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break

        if entrada.lstrip('-').isdigit():
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é par.")
            else:
                impares += 1
                print(f"{numero} é ímpar.")
        else:
            print("Entrada inválida. Por favor, digite um número válido.")

    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

classificar_numeros()
