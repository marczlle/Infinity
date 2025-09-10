produtos = {}

for i in range(5):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_produto = float(input(f"Digite o preço de {nome_produto}: "))
    produtos[nome_produto] = preco_produto

valor_total = sum(produtos.values())

print("\nResumo da compra:")
for nome, preco in produtos.items():
    print(f"{nome}: R${preco:.2f}")

print(f"\nValor total da compra: R${valor_total:.2f}")
