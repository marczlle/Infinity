# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir 
# o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado 
# ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, 
# suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

num_alunos = int(input("Digite o número de alunos: "))
somageral = 0

# itera sobre os alunos
for i in range(num_alunos):
    nome_aluno = input(f"\nDigite o nome do aluno {i + 1}: ")

    # solicita notas
    nota1 = float(input(f"Digite a nota 1 de {nome_aluno}: "))
    nota2 = float(input(f"Digite a nota 2 de {nome_aluno}: "))
    nota3 = float(input(f"Digite a nota 3 de {nome_aluno}: "))

    # calcula média do aluno
    media = (nota1 + nota2 + nota3) / 3
    somageral += media

    # verifica se aluno foi aprovado ou reprovado
    if media >= 7.0:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    # exibe as informações do aluno
    print(f"""\nNome: {nome_aluno}
    Notas: {nota1}, {nota2}, {nota3}
    Média: {media:.2f}")
    Resultado: {resultado}""")

# calcula e exibe a média geral da turma
mediageral = somageral / num_alunos
print(f"\nA média geral da turma é: {mediageral:.2f}")
