from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get content length
        content_length = int(self.headers['Content-Length'])
        # Read text data
        text_data = self.rfile.read(content_length).decode('utf-8')
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Log to file
        try:
            with open('logs.txt', 'a') as f:
                f.write(f"{timestamp}: {text_data}\n")
            
            # Send success response
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Log saved successfully".encode())
        except Exception as e:
            # Send error response
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

# Start server
HOST = '0.0.0.0'
PORT = 8000
server = HTTPServer((HOST, PORT), LogHandler)
print(f"Server started at http://{HOST}:{PORT}")
server.serve_forever()