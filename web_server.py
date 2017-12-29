from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import entertainment_center

PORT_NUMBER = 8080

#This class will handles any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        #Open the static file requested and send it
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'fresh_tomatoes.html')
        f = open(my_file) 
        self.wfile.write(f.read())
        f.close()
        return

try:
    #Before Starting web server, create the static web page of movies
    entertainment_center.load_movies()
    
    #Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()