import time
import subprocess
from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler): # type: ignore
    def on_modified(self, event):
        if event.src_path.endswith(".py"):  # Detecta alterações nos arquivos .py
            print(f"Arquivo {event.src_path} modificado. Reiniciando o bot...")
            # Reinicia o bot
            subprocess.Popen(["python", "bot.py"])  # Usa Popen para evitar bloqueios

if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path="./", recursive=True)  # Caminho do diretório do bot
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    