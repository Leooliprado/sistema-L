import shutil
import os
import time
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.spinner import Spinner
from rich.live import Live

from servidor import iniciar_sistema

console = Console()

# ======================
# FUNÇÕES DE ANIMAÇÃO
# ======================

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def animacao_transicao(texto="Carregando...", tempo=1):
    spinner = Spinner("dots", text=f"[bold yellow]{texto}[/]", style="yellow")
    with Live(spinner, refresh_per_second=12, console=console):
        time.sleep(tempo)
    limpar_tela()

def texto_digitando(texto, delay=0.02, estilo="bold yellow"):
    for char in texto:
        console.print(char, style=estilo, end="")
        time.sleep(delay)
    print()

# ======================
# LOGO
# ======================

logo = """
░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░░░░░░░██╗░░░░░
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗░░░░░░██║░░░░░
╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║█████╗██║░░░░░
░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║╚════╝██║░░░░░
██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║░░░░░░███████╗
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░░░░╚══════╝
"""

cores = ["#FFD700", "#FFC107", "#FFB300", "#FFA000"]
width = shutil.get_terminal_size().columns

text = Text()
linhas = logo.strip().split("\n")
max_length = max(len(linha) for linha in linhas)
spaces = (width - max_length) // 2

for i, linha in enumerate(linhas):
    cor = cores[i % len(cores)]
    text.append(" " * spaces + linha + "\n", style=f"bold {cor}")

descricao = """
Bem-vindo ao Sistema-L! Este é um sistema dedicado a fornecer serviços de alta qualidade para desenvolvedores e entusiastas de tecnologia. Aqui você encontrará ferramentas, recursos e uma comunidade ativa para ajudá-lo em seus projetos. Explore, colabore e cresça conosco!
"""

# ======================
# EXECUÇÃO INICIAL
# ======================

limpar_tela()
console.print("\n" * 2)
console.print(text)
console.print("\n")

console.print(
    Panel(
        descricao,
        style="bold black on yellow",
        title="[bold #FFD700]Sistema-L[/]",
        subtitle="[bold #FFC107]Tecnologia e Inovação[/]",
        width=width
    )
)

console.print()
texto_digitando("Pressione Enter para continuar...")
input()

animacao_transicao("Entrando no sistema...")
iniciar_sistema()

