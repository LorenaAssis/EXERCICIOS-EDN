def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
valor = 150.00
porcentagem = 10
print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")