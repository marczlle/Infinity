from faker import Faker
import random

fake = Faker('pt-BR')

generos = [
    {'id': 1, 'nome': '', 'genero': 'acao', 'classificacao': 0, 'filmes': []},
    {'id': 2, 'nome': '', 'genero': 'comedia', 'classificacao': 0, 'filmes': []},
    {'id': 3, 'nome': '', 'genero': 'drama', 'classificacao': 0, 'filmes': []},
    {'id': 4, 'nome': '', 'genero': 'suspense', 'classificacao': 0, 'filmes': []},
    {'id': 5, 'nome': '', 'genero': 'ficcao', 'classificacao': 0, 'filmes': []}
]

for genero in generos:
    for i in range(3):
        novo_filme = {
            'id': len(genero['filmes']) + 1,
            'nome': fake.catch_phrase(),
            'genero': genero['genero'],
            'classificacao': random.randint(1, 10)
        }
        genero['filmes'].append(novo_filme)

def adicionarfilme(novonome, generoescolhido, novaclassificacao):
    global generos
    genero_encontrado = False
    
    for genero in generos:
        if genero['genero'] == generoescolhido:
            novo_filme = {
                'id': len(genero['filmes']) + 1,
                'nome': novonome,
                'genero': generoescolhido,
                'classificacao': novaclassificacao
            }
            genero['filmes'].append(novo_filme)
            genero_encontrado = True
            print(f"Filme '{novonome}' adicionado com sucesso no gênero '{generoescolhido}'!")
            break
    
    if not genero_encontrado:
        print(f"Erro: O gênero '{generoescolhido}' não foi encontrado!")

def recomendacaofilme(generoinformado):
    filmes_do_genero = []
    
    for genero in generos:
        if genero['genero'] == generoinformado:
            filmes_do_genero = genero['filmes']
            break
    
    if filmes_do_genero:
        filmes_recomendados = random.sample(filmes_do_genero, 3)
        print(f"Recomendando filmes do gênero '{generoinformado}':")
        for filme in filmes_recomendados:
            print(f"  Nome: {filme['nome']}, Classificação: {filme['classificacao']}")
    else:
        print(f"Erro: O gênero '{generoinformado}' não foi encontrado!")

def removerfilme(nomefilmedel):
    global generos
    for genero in generos:
        for filme in genero['filmes']:
            if filme['nome'] == nomefilmedel:
                genero['filmes'].remove(filme)
                print(f"Filme '{nomefilmedel}' deletado com sucesso!")
                return
    print(f"Erro: O filme '{nomefilmedel}' não foi encontrado.")

def exibir_filmes():
    if not any(genero['filmes'] for genero in generos):
        print("Nenhum filme cadastrado.")
        return

    print("Lista de Filmes Cadastrados:\n")
    for genero in generos:
        print(f"Gênero: {genero['genero']}")
        for filme in genero['filmes']:
            print(f"  ID: {filme['id']}, Nome: {filme['nome']}, Gênero: {filme['genero']}, Classificação: {filme['classificacao']}")
        print() 

def main():
    while True:
        print('''Bem-vindo ao Sistema de Recomendação de Filmes!

        Escolha uma opção:
        1. Adicionar um novo filme
        2. Recomendar filmes por gênero
        3. Remover um filme pelo nome
        4. Exibir todos os filmes cadastrados
        5. Sair''')
        
        opcao = input("Digite uma opção: ")
        
        if opcao == '1':
            nomenovogenero = input("Digite o gênero do filme: ")
            nomenovofilme = input("Digite o nome do filme: ")
            novaclassificacao = int(input("Digite uma nota para o filme (1 a 10): "))
            
            adicionarfilme(nomenovofilme, nomenovogenero, novaclassificacao)
        elif opcao == '2':
            generorec = input('Digite o gênero de interesse: ')
            recomendacaofilme(generorec)
        elif opcao == '3':
            deletar = input('Digite o nome do filme que você quer deletar: ')
            removerfilme(deletar)
        elif opcao == '4':
            exibir_filmes()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print('Opção inválida! Tente novamente.')

main()
