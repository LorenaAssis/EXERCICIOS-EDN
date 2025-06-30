def calcular_preco_final(preco_original, porcentagem_desconto):
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)

# Interação com usuário
preco = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto: "))

preco_final = calcular_preco_final(preco, desconto)
print(f"Preço final após desconto: R$ {preco_final:.2f}")
