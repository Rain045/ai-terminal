import click
import asyncio
import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from .ollama_client import OllamaClient
from .context_engine import ContextEngine
from .terminal import Terminal

console = Console()
terminal = Terminal()

def run_command_with_pty(command):
    """Executes a command using the PTY terminal."""
    if not command:
        return
    console.print(f"[bold dim]> {command}[/bold dim]")
    terminal.execute(command)

async def handle_intent(prompt, client, engine):
    """Processes user intent, generates a command, and asks for confirmation."""
    context = engine.format_context_for_llm()
    # Briefly show environment summary
    env_summary = " | ".join([line.strip() for line in context.split("\n") if line.strip()])
    console.print(f"[dim italic]Env: {env_summary}[/dim italic]")
    
    with console.status("[bold blue]AI is thinking...[/bold blue]"):
        command = await client.generate_command(prompt, context)
    
    if command.startswith("Error"):
        console.print(f"[red]{command}[/red]")
        return

    console.print(Panel(f"[bold yellow]{command}[/bold yellow]", title="AI Generated Command"))
    
    action = click.prompt(
        "Execute (y), Edit (e), or Skip (s)?",
        type=click.Choice(['y', 'e', 's'], case_sensitive=False),
        default='y'
    )
    
    if action == 'y':
        run_command_with_pty(command)
    elif action == 'e':
        edited_command = click.edit(command)
        if edited_command:
            run_command_with_pty(edited_command.strip())
    else:
        console.print("[dim]Command skipped.[/dim]")

@click.command()
@click.argument('prompt', required=False)
def main(prompt):
    """AI Terminal: Optimized for local LLMs and system awareness."""
    client = OllamaClient()
    engine = ContextEngine()
    
    async def async_main():
        if prompt:
            await handle_intent(prompt, client, engine)
        else:
            console.print("[bold green]Welcome to AI Terminal (Local Mode)![/bold green]")
            console.print("Aware of: [cyan]Ubuntu, Docker, Conda[/cyan]. Using: [magenta]Ollama[/magenta]")
            console.print("Commands: [bold yellow]'!'[/bold yellow] for shell, [bold yellow]'exit'[/bold yellow] to quit.")
            
            while True:
                try:
                    user_input = console.input("[bold cyan]> [/bold cyan]")
                    if not user_input.strip():
                        continue
                    if user_input.lower() in ('exit', 'quit'):
                        break
                    
                    if user_input.startswith('!'):
                        run_command_with_pty(user_input[1:])
                    else:
                        await handle_intent(user_input, client, engine)
                        
                except EOFError:
                    break

    asyncio.run(async_main())

if __name__ == '__main__':
    main()
