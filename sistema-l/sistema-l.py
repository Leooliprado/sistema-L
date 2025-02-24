import shutil
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

from servidor import iniciar_sistema



console = Console()

logo = """
░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░░░░░░░██╗░░░░░
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗░░░░░░██║░░░░░
╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║█████╗██║░░░░░
░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║╚════╝██║░░░░░
██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║░░░░░░███████╗
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░░░░╚══════╝
"""

# Cores douradas e amarelas para um efeito mesclado
cores = ["#FFD700", "#FFC107", "#FFB300", "#FFA000"]

# Calcular a largura do terminal automaticamente
width = shutil.get_terminal_size().columns

# Criar o texto com cores mescladas
text = Text()
linhas = logo.strip().split("\n")

# Centralizando o texto na largura do terminal
max_length = max(len(linha) for linha in linhas)
spaces = (width - max_length) // 2  # Calcular os espaços para centralizar

for i, linha in enumerate(linhas):
    cor = cores[i % len(cores)]  # Alterna entre as cores
    text.append(" " * spaces + linha + "\n", style=f"bold {cor}")

# Descrição do servidor
descricao = """
Bem-vindo ao servidor Gistma! Este é um servidor dedicado a fornecer
serviços de alta qualidade para desenvolvedores e entusiastas de tecnologia.
Aqui você encontrará ferramentas, recursos e uma comunidade ativa para
ajudá-lo em seus projetos. Explore, colabore e cresça conosco!
"""

# Exibir a logo e a descrição apenas uma vez
print("\n" * 2)
console.print(text)
print("\n" * 2)
console.print(
    Panel(
        descricao,
        style="bold black on yellow",  # Texto preto com fundo amarelo
        title="[bold #FFD700]Descrição do Servidor[/]",  # Título em dourado
        subtitle="[bold #FFC107]Gistma - Tecnologia e Inovação[/]",  # Subtítulo em amarelo
        width=width
    )
)

# Pausa para o usuário pressionar Enter
console.print("\n[bold]Pressione Enter para continuar...[/]", style="bold yellow")
input()

iniciar_sistema()

