import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8081
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    # Force socket reuse to avoid "address already in use" errors on restarts
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==================================================================")
        print("🚀 Campus Club Membership Service - Broken Access Control Practical Demo Server")
        print("==================================================================")
        print(f"🇹🇭 เซิร์ฟเวอร์เริ่มต้นแล้วที่: http://localhost:{PORT}")
        print("   กรุณากดเปิดเบราว์เซอร์ และทำตามขั้นตอน:")
        print("   1. คลิกปุ่ม 'View My Registration' เพื่อดูข้อมูลของ Bob (Member)")
        print("   2. เปิดแท็บใหม่แล้วแก้ URL เป็น .../data/registration-1.json")
        print("   3. สังเกตว่าไม่มีการตรวจสอบสิทธิ์ใด ๆ — Bob เข้าถึงข้อมูลระดับ Officer ของ Alice ได้ทันที")
        print("------------------------------------------------------------------")
        print(f"🇬🇧 Local server started at: http://localhost:{PORT}")
        print("   Please open the page in your browser and follow these steps:")
        print("   1. Click 'View My Registration' to load Bob's (Member) own record.")
        print("   2. Open a new tab and edit the URL to .../data/registration-1.json")
        print("   3. Notice there is no authorisation check at all — Bob can read")
        print("      Alice's Officer-level permissions just by guessing the file name.")
        print("==================================================================")
        print("Press Ctrl+C to stop the server / กด Ctrl+C เพื่อหยุดเซิร์ฟเวอร์")

        # Open default browser
        webbrowser.open(f"http://localhost:{PORT}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            sys.exit(0)

if __name__ == "__main__":
    run()
