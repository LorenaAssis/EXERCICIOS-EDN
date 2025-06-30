from datetime import datetime

def calcular_dias_vivo(data_nascimento):
    hoje = datetime.today()
    dias_vivo = (hoje - data_nascimento).days
    return dias_vivo

# Entrada da data de nascimento no formato dd/mm/aaaa
data_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nasc = datetime.strptime(data_str, "%d/%m/%Y")

dias = calcular_dias_vivo(data_nasc)
print(f"Você está vivo há {dias} dias.")
