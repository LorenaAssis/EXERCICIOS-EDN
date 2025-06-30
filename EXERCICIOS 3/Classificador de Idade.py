# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Classificação da idade
if 0 <= idade <= 12:
    print("Você é Criança.")
elif 13 <= idade <= 17:
    print("Você é Adolescente.")
elif 18 <= idade <= 59:
    print("Você é Adulto.")
elif idade >= 60:
    print("Você é Idoso.")
else:
    print("Idade inválida.")