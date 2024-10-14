#variaveis
numero_fixo = 7
limite_tentativas = 3

print("Bem-vindo ao jogo! Tente adivinhar o número.")
#só entra no loop se ainda tiver tentativas
while limite_tentativas > 0:

    palpite = int(input("Digite seu palpite: "))

    if palpite != numero_fixo:
        print("Você errou! Tente novamente.")
        #subtrai das tentativas caso o usuário erre
        limite_tentativas -=1
    else:
        print(f"Você acertou, parabéns! O número era {numero_fixo}")
        #sai do loop quando acerta
        break
else:
    print("Lamento! Acabaram suas tentativas.")
