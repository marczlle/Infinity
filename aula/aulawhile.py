# preco_produto = float(input("Digite o preço do produto: "))
# qtd_produto = int(input("Digite a quantidade do produto: "))


# if qtd_produto > 10:
#     valor_desconto = preco_produto * 0.1
#     preco_desconto = preco_produto - valor_desconto
#     print(f'Valor total com desconto: {preco_desconto}')
# else:
#     print(f'Valor total: {preco_produto}') 


# atividade while

# Crie um programa que use um laço while
# para contar de 1 a 10 e exibir cada número.

# num = 1

# while num < 11:
#     print(num)
#     num +=1



# Escreva um programa que use um laço while para
# somar os números de 1 a 100 e exiba o resultado.

# soma = 0
# num = 1

# while num <= 100:
#     soma += num
#     num +=1

# print(soma)


# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

# numero_usuario = int(input("Digite o número: ")) 
# contador = 1

# while contador < 11:
#     print(f'{contador} x {numero_usuario} = {numero_usuario * contador}')
#     contador +=1



# Desenvolva um programa que use um laço while para exibir
# uma contagem regressiva de 10 até 1 e, em seguida, exiba
# "Feliz Ano Novo!".

# num = 10

# while num > 0:
#     print(f'{num}')
#     num -=1

# print('Feliz ano novo!')


# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.

# numero = int(input('Digite o número que você quer: '))
# contador = 1

# while contador <= numero:
#     if contador %2 != 0:
#         print(contador)
#     contador+=1


# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.


while True:
    numero_digitado = int(input("Digite o número que você quer: "))
    novo_digitado = int(input('Digite outro número: '))
    if numero_digitado > 0 and novo_digitado > 0:
        soma = novo_digitado + numero_digitado
    else: 
        break
print(f'Resultado da soma é: {soma}')

# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.



# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.
