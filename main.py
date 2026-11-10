"""Desktop Detective — локальный сервер для запуска игры."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "frontend"
HOST, PORT = "127.0.0.1", 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB), **kwargs)
    def log_message(self, fmt, *args):
        print("[Desktop Detective] " + (fmt % args))

def main():
    if not WEB.exists():
        raise SystemExit("Не найдена папка frontend.")
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}"
    print("Desktop Detective запущен:", url)
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nИгра остановлена.")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
