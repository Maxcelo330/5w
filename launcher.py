# launcher.py
import threading, webbrowser, sys, os, socket
import streamlit.web.cli as stcli

def find_free_port():
    s = socket.socket()
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

def run_streamlit(app_path, port):
    sys.argv = ["streamlit", "run", app_path, "--server.headless=true", f"--server.port={port}"]
    stcli.main()

if __name__ == "__main__":
    # Cuando esté empacado con PyInstaller, los archivos añadidos via --add-data
    # se extraen en sys._MEIPASS
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    app_path = os.path.join(base, "app.py")  # pyinstaller debe incluir app.py como data
    port = find_free_port()
    threading.Thread(target=run_streamlit, args=(app_path, port), daemon=True).start()
    webbrowser.open(f"http://localhost:{port}")
