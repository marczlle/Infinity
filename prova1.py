print("Bem vindo!")

# variáveis que vão ser inputadas para o usuário, que restrigem a ser um float:
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

# exibe o resultado da conta da área (base*altura), e limita as casa decimais pós o ponto.
print(f"O total da área é de: {base*altura:.2f}m²")
