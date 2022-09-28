### File to create a locally (first) camera hosting system, then a web hosted system. 
# Python 3 server example

### USE FOR LOCAL HOST TESTING. NOW UP ON adamgulde.github.io
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

# httpd.shutdown()