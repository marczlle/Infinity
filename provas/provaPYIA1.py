contato = {}

contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o número de telefone do contato: ")
contato['email'] = input("Digite o email do contato: ")

print("\nInformações do Contato:")
for chave, valor in contato.items():
    print(f"{chave.capitalize()}: {valor}")
