import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    # Force socket reuse to avoid "address already in use" errors on restarts
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==================================================================")
        print("🚀 Prompt Sanitizer (from NU MOOC 084 — Cybersecurity Awareness)")
        print("==================================================================")
        print(f"Local server started at: http://localhost:{PORT}")
        print("Open the page in your browser to play through the activity.")
        print("==================================================================")
        print("Press Ctrl+C to stop the server")

        # Open default browser
        webbrowser.open(f"http://localhost:{PORT}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            sys.exit(0)

if __name__ == "__main__":
    run()
