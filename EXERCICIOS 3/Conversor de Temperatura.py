def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def fahrenheit_para_kelvin(f):
    c = fahrenheit_para_celsius(f)
    return celsius_para_kelvin(c)

def kelvin_para_fahrenheit(k):
    c = kelvin_para_celsius(k)
    return celsius_para_fahrenheit(c)

# Entrada do usuário
temp = float(input("Digite o valor da temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
unidade_destino = input("Digite a unidade para a qual deseja converter (C, F ou K): ").strip().upper()

# Conversão
if unidade_origem == unidade_destino:
    temp_convertida = temp
elif unidade_origem == 'C':
    if unidade_destino == 'F':
        temp_convertida = celsius_para_fahrenheit(temp)
    elif unidade_destino == 'K':
        temp_convertida = celsius_para_kelvin(temp)
elif unidade_origem == 'F':
    if unidade_destino == 'C':
        temp_convertida = fahrenheit_para_celsius(temp)
    elif unidade_destino == 'K':
        temp_convertida = fahrenheit_para_kelvin(temp)
elif unidade_origem == 'K':
    if unidade_destino == 'C':
        temp_convertida = kelvin_para_celsius(temp)
    elif unidade_destino == 'F':
        temp_convertida = kelvin_para_fahrenheit(temp)
else:
    print("Unidade de origem inválida.")
    temp_convertida = None

# Exibição do resultado
if temp_convertida is not None:
    print(f"{temp}°{unidade_origem} equivale a {temp_convertida:.2f}°{unidade_destino}")