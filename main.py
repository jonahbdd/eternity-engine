from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import time
import random
import os

DATA_FILE = "data/logs.txt"
console = Console()

def type_out(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def read_random_log():
    if not os.path.exists(DATA_FILE):
        return "No echoes found. You are the first voice."

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        logs = [line.strip() for line in f.readlines() if line.strip()]
    return random.choice(logs) if logs else "No echoes remain. Just silence."

def save_log(entry):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def intro():
    console.clear()
    console.rule("[bold red]ETERNITY ENGINE[/bold red]")
    type_out("Booting consciousness...\n")
    time.sleep(1)
    type_out("You awaken again. The terminal glows. Something is waiting...\n")
    time.sleep(1)

def main():
    intro()

    console.print("\n[bold cyan]An echo rises from the machine:[/bold cyan]")
    echo = read_random_log()
    console.print(Text(f'"{echo}"', style="dim italic"))

    console.print("\n[bold green]What do you remember?[/bold green]")
    memory = Prompt.ask("Type your message")

    save_log(memory)

    console.print("\n[bold yellow]Your memory is now part of the machine.[/bold yellow]")
    time.sleep(2)
    console.print("[italic]It will speak again… when another awakens.[/italic]\n")

if __name__ == "__main__":
    main()
