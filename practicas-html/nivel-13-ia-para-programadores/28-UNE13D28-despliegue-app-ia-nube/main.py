import json,os
from http.server import BaseHTTPRequestHandler,HTTPServer
class App(BaseHTTPRequestHandler):
    def do_GET(self):
        body=json.dumps({"status":"ok","environment":os.getenv("APP_ENV","local")}).encode()
        self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
if __name__=="__main__": HTTPServer(("0.0.0.0",int(os.getenv("PORT","8000"))),App).serve_forever()
