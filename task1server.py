from http.server import HTTPServer, BaseHTTPRequestHandler
import time
HOST= "localhost"
PORT= 3000

class myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(bytes('{"slackUsername":"Agbani", "backend":True, "age":21, "bio":"Python developer that likes food"}', 'utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((HOST, PORT), myserver)
    print("Server started")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server closed")