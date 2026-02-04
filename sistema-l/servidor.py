import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.live import Live

console = Console()

# ======================
# FUNÇÕES DE APOIO
# ======================

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def animacao(texto, tempo=1):
    spinner = Spinner("dots", text=f"[bold yellow]{texto}[/]", style="yellow")
    with Live(spinner, refresh_per_second=12, console=console):
        time.sleep(tempo)
        limpar_tela()

# ======================
# FUNÇÕES DO MENU
# ======================

def exibir_menu():
    menu = """
[bold]1[/] - Iniciar Servidor
[bold]2[/] - Parar Servidor
[bold]3[/] - Ver Status
[bold]4[/] - Sair
"""
    console.print(
        Panel(
            menu.strip(),
            style="bold black on yellow",
            title="[bold #FFD700]Menu Principal[/]"
        )
    )

def iniciar_servidor():
    animacao("Iniciando servidor...")
    try:
        # Exemplo: Executar um comando para iniciar o servidor
        console.print("[bold green]✔ Servidor iniciado com sucesso![/]")
    except Exception as e:
        console.print(f"[bold red]Erro ao iniciar o servidor: {e}[/]")

def parar_servidor():
    console.print(
        Panel(
            "[bold black]Deseja realmente parar o servidor?[/]\n\n"
            "[bold black]S[/] - Sim\n"
            "[bold black]N[/] - Não",
            title="[bold red]Confirmação[/]",
            style="bold black on yellow"
        )
    )

    resposta = Prompt.ask("Escolha", choices=["s", "n"])

    if resposta.lower() == "n":
        console.print("[bold cyan]❌ Operação cancelada.[/]")
        time.sleep(1)
        return

    animacao("Parando servidor...")
    try:
        console.print("[bold red]✔ Servidor parado com sucesso![/]")
    except Exception as e:
        console.print(f"[bold red]Erro ao parar o servidor: {e}[/]")

def verificar_status():
    animacao("Verificando status...")
    try:
        console.print("[bold cyan]✔ Status: Servidor ATIVO[/]")
    except Exception as e:
        console.print(f"[bold red]Erro ao verificar status: {e}[/]")

# ======================
# LOOP PRINCIPAL
# ======================

def iniciar_sistema():
    while True:
        limpar_tela()
        exibir_menu()

        escolha = Prompt.ask(
            "\n[bold yellow]Digite uma opção[/]", 
            choices=["1", "2", "3", "4"]
        )

        if escolha == "1":
            iniciar_servidor()
        elif escolha == "2":
            parar_servidor()
        elif escolha == "3":
            verificar_status()
        elif escolha == "4":
            animacao("Encerrando sistema...")
            console.print("[bold yellow]Até logo 👋[/]")
            time.sleep(1)
            break

        console.print("\nPressione Enter para voltar ao menu...", style="bold yellow")
        input()

