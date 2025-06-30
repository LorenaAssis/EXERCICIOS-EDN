def media_turma():
    notas = []
    quantidade = int(input("Quantas notas deseja registrar? "))

    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = sum(notas) / quantidade if quantidade > 0 else 0
    print(f"A média da turma é: {media:.2f}")

media_turma()
