import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    # Force socket reuse to avoid "address already in use" errors on restarts
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==================================================================")
        print("🚀 Campus Club Membership Service - Data Minimisation Practical Demo Server")
        print("==================================================================")
        print(f"🇹🇭 เซิร์ฟเวอร์เริ่มต้นแล้วที่: http://localhost:{PORT}")
        print("   กรุณากดเปิดเบราว์เซอร์ และทำตามขั้นตอนการสอนสไลด์ที่ 5:")
        print("   1. เปิด Inspect (F12) และไปที่แท็บ 'Network'")
        print("   2. คลิกปุ่ม 'Load Attendance List' บนหน้าเว็บ")
        print("   3. ดับเบิ้ลคลิกดูไฟล์ 'attendance.json' ในแท็บ Network เพื่อดูข้อมูลที่รั่วไหล")
        print("------------------------------------------------------------------")
        print(f"🇬🇧 Local server started at: http://localhost:{PORT}")
        print("   Please open the page in your browser and check Slide 5:")
        print("   1. Open DevTools (F12) and go to the 'Network' tab.")
        print("   2. Click 'Load Attendance List' on the webpage.")
        print("   3. Select 'attendance.json' to inspect the leaked background payload.")
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
