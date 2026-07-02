import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8082
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==================================================================")
        print("🚀 Campus Club Security vs Usability Trade-off Demo Server")
        print("==================================================================")
        print(f"🇹🇭 เซิร์ฟเวอร์เริ่มต้นแล้วที่: http://localhost:{PORT}")
        print(f"🇬🇧 Local server started at: http://localhost:{PORT}")
        print("==================================================================")
        print("Press Ctrl+C to stop the server / กด Ctrl+C เพื่อหยุดเซิร์ฟเวอร์")
        
        webbrowser.open(f"http://localhost:{PORT}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            sys.exit(0)

if __name__ == "__main__":
    run()
