from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import requests

# In-memory store for short_name -> long URI mappings
url_mapping = {}

class BookmarkServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        print(parsed_path)
        # Root path: Serve the HTML form
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <body>
                    <h2>Create a Shortened URL</h2>
                    <form method="POST">
                        Long URL: <input name="long_url"><br>
                        Short name: <input name="short_name"><br>
                        <input type="submit" value="Shorten">
                    </form>
                </body>
                </html>
            """)
        else:
            # Short URI path: Redirect to the corresponding long URI
            short_name = parsed_path.path[1:]  # Strip the leading '/'
            if short_name in url_mapping:
                self.send_response(302)
                self.send_header("Location", url_mapping[short_name])
                self.end_headers()
            else:
                self.send_error(404, "Short URL not found")
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        form_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
        
        long_url = form_data.get('long_url', [None])[0]
        short_name = form_data.get('short_name', [None])[0]
        
        if not long_url or not short_name:
            self.send_error(400, "Both long_url and short_name fields are required")
            return
        
        # Verify the long URL exists
        try:
            response = requests.get(long_url)
            if response.status_code == 200:
                url_mapping[short_name] = long_url
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"""
                    <html>
                    <body>
                        <h2>Success!</h2>
                        <p>Short URL: <a href="/{short_name}">/{short_name}</a></p>
                    </body>
                    </html>
                """.encode('utf-8'))
            else:
                self.send_error(404, "The long URL does not exist")
        except requests.RequestException:
            self.send_error(404, "The long URL is invalid or cannot be reached")

def run(server_class=HTTPServer, handler_class=BookmarkServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting bookmark server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
