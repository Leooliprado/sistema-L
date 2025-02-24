import os
import subprocess
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt
import time


console = Console()

def iniciar_sistema():

    def exibir_menu():
        # Texto do menu
        menu_texto = """
        [bold]Escolha uma opção:[/]
        1. Iniciar Servidor
        2. Parar Servidor
        3. Ver Status do Servidor
        4. Sair
        """
        
        # Exibir o menu dentro de um painel amarelo
        console.print(
            Panel(
                menu_texto,
                style="bold black on yellow",  # Texto preto com fundo amarelo
                title="[bold #FFD700]Menu do Servidor[/]",  # Título em dourado
            )
        )

        print("\n")

    def iniciar_servidor():
        console.print("\n[bold #FFD700]Iniciando o servidor...[/]")  # Dourado
        try:
            # Exemplo: Executar um comando para iniciar o servidor
            console.print("[bold #32CD32]Servidor iniciado com sucesso![/]")  # Verde limão
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Erro ao iniciar o servidor: {e}[/]")

    def parar_servidor():
        console.print("\n[bold #FFA500]Parando o servidor...[/]")  # Laranja
        try:
            # Exemplo: Executar um comando para parar o servidor
            console.print("[bold #FF4500]Servidor parado com sucesso![/]")  # Vermelho laranja
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Erro ao parar o servidor: {e}[/]")

    def verificar_status():
        console.print("\n[bold #1E90FF]Verificando status do servidor...[/]")  # Azul claro
        try:
            # Exemplo: Executar um comando para verificar o status
            console.print("[bold #00CED1]Status: Servidor ativo![/]")  # Azul turquesa
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Erro ao verificar status: {e}[/]")

    # Loop principal
    while True:
        # Limpar o terminal antes de exibir o menu
        os.system("cls" if os.name == "nt" else "clear")
        
        exibir_menu()
        
        # Exibir o texto do prompt com estilo "bold yellow"
        console.print("Digite o número da opção", style="bold yellow", end=" ")
        
        # Capturar a escolha do usuário
        escolha = Prompt.ask(choices=["1", "2", "3", "4"])

        if escolha == "1":
            iniciar_servidor()
        elif escolha == "2":
            parar_servidor()
        elif escolha == "3":
            verificar_status()
        elif escolha == "4":
            print("\n")
            console.print("[bold yellow]Saindo...[/]")
            print("\n")
            time.sleep(1.5)
            os.system("cls" if os.name == "nt" else "clear")
            break

        # Pausa antes de retornar ao menu
        console.print("\n[bold]Pressione Enter para continuar...[/]", style="bold yellow")
        input()