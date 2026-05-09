from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = """
        <html>
        <head>
            <title>Google App Engine</title>
        </head>
        <body>
            <h1>Welcome to Google App Engine</h1>
            <p>Simple Python Web Application</p>   
        </body>
        </html>
        """

        self.wfile.write(message.encode())

PORT = 8080

server = HTTPServer(("0.0.0.0", PORT), MyServer)

print("Server running on port", PORT)

server.serve_forever()
