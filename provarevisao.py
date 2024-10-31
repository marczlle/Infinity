
# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir 
# o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado 
# ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, 
# suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

num_alunos = int(input("Digite o número de alunos: "))

# itera sobre os alunos
for i in range(num_alunos):
    nome_aluno = input(f"\nDigite o nome do aluno {i + 1}: ")

    # solicita as três notas
    nota1 = float(input(f"Digite a nota 1: "))
    nota2 = float(input(f"Digite a nota 2: "))
    nota3 = float(input(f"Digite a nota 3: "))

    # calcula a média do aluno
    media = (nota1 + nota2 + nota3) / 3

    # verifica aprovação
    if media >= 7.0:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    # exibe as informações do aluno
    print(f"\nNome: {nome_aluno}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {resultado}")
