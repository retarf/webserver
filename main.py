from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# https://flaviocopes.com/python-http-server/

ADDRESS = ""
PORT = 8000


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Best-language', 'PYTHON')
        self.end_headers()

        message = {"message": "Hello world!"}
        json_message = json.dumps(message)
        self.wfile.write(bytes(json_message, "utf8"))


with HTTPServer((ADDRESS, PORT), handler) as server:
    server.serve_forever()
