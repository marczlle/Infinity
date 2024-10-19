#variáveis
numeroinicial = int(input("Digite onde quer que inicie o intervalo: "))
numerofinal = int(input("Digite onde quer que termine o intervalo: "))
soma = 0

# itera todos os números do inicio do intervalo ao fim dele
for i in range(numeroinicial, numerofinal + 1): # +1 pq quero que ele inclua o último número na iteraação também
    if i % 2 == 0: # confere se é par
        soma = soma + i 
    else:
        continue # caso o número não seja par, ele pula pra próxima iteração

print(f"A soma total de números pares é: {soma}")
