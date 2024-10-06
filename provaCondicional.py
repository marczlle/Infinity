# número limitado a float digitado pelo usuário para descobrir sua natureza.
numero_digitado = float(input("Digite um número: "))

# estrutura condicional para verificar se o número é maior ou menor que zero, caso não seja nem maior nem menor, então ele é zero.
if numero_digitado > 0:
    print(f"O número digitado: {numero_digitado} é um número positivo.")
elif numero_digitado < 0:
    print(f"O número digitado: {numero_digitado} é negativo.")
else:
    print(f"O número digitado é zero.")
