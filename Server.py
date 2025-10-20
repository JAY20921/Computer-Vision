import http.server
import socketserver
import os

PORT = 8000  # You can change this to any available port

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Change to the directory where you want to serve files from
os.chdir(r"C:\Users\acer\Desktop\Capture")  # Replace with your directory path

handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving at port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Server stopped.")
    httpd.server_close()