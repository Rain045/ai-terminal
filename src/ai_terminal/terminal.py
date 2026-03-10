import ptyprocess
import sys
import os
import signal
from rich.console import Console

console = Console()

class Terminal:
    def execute(self, command):
        """Executes a command using a pseudo-terminal (PTY)."""
        if not command:
            return

        try:
            # Spawn the command in a PTY
            p = ptyprocess.PtyProcessUnicode.spawn(command.split())
            
            # Helper to handle terminal resizing
            def handle_resize(signum, frame):
                rows, cols = console.size
                p.setwinsize(rows, cols)

            signal.signal(signal.SIGWINCH, handle_resize)
            handle_resize(None, None)

            while p.isalive():
                try:
                    # Read from PTY and write to stdout
                    output = p.read(1024)
                    if output:
                        sys.stdout.write(output)
                        sys.stdout.flush()
                except EOFError:
                    break
                
            p.close()
            
        except Exception as e:
            console.print(f"[bold red]Terminal Error:[/bold red] {e}")
