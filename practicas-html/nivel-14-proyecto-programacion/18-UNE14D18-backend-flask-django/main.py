import json
from http.server import BaseHTTPRequestHandler,HTTPServer
class API(BaseHTTPRequestHandler):
    def do_GET(self):
        body=json.dumps({"servicio":"solicitudes","status":"ok"}).encode();self.send_response(200);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(body)));self.end_headers();self.wfile.write(body)
if __name__=="__main__": HTTPServer(("127.0.0.1",8000),API).serve_forever()
