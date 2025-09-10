import flet as ft

def main(page: ft.Page):
    lista_tarefas = ft.Column()

    # função para adicionar a tarefa à lista
    def adicionar_tarefa(e):
        nome_tarefa = campo_tarefa.value
        if nome_tarefa:
            lista_tarefas.controls.append(ft.Text(nome_tarefa))
            campo_tarefa.value = ""  # limpar
            page.update() 

    campo_tarefa = ft.TextField(label="Digite uma tarefa", autofocus=True)
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)

    #fazendo a lista
    page.add(campo_tarefa, botao_adicionar, lista_tarefas)

# iniciando aplicação
ft.app(target=main)
