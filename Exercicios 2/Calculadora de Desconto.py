# Dados do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20  # em %

# Cálculo do valor do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

# Cálculo do preço final com desconto
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("Produto:", nome_produto)
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")