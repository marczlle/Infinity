# Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar 
# o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, 
# o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa 
# deve terminar imediatamente.

# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma 
# mensagem de "Acesso bloqueado" repetida três vezes.

usuario = "usuario123"
senha = "123"

# Tentativas de login
for tentativa in range(3):
    usuariotent = input("Digite o nome de usuário: ")
    senhatent = input("Digite a senha: ")

    # condição para verficiar
    if usuario == usuariotent and senha == senhatent:
        print(f"Bem-vindo, {usuario}!")
        break 
    else:
        tentativas_restantes = 2 - tentativa
        if tentativas_restantes > 0:
            print(f"Algo está errado. Você ainda tem {tentativas_restantes} tentativas.")
        else:
                print("Acesso bloqueado.")
