#!/usr/bin/env python2
from __future__ import print_function
import heart
import logging
import datetime
import thread
import time
import json
import numpy as np
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
 
class HttpServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
       
        if self.path=="/stats.json":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(self.server.handler.json_stats())

        else:
            f = open("."+ self.path)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(f.read())
            f.close()
        
        return

class MyHTTPServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, handler):
        HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.handler = handler
             
class HttpServer:
    # http://fw-geekycoder.blogspot.com/2012/05/how-to-pass-some-arguments-to.html
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server = None
         
    def start(self):
        logging.info('Starting at %s:%d' % ( self.host, self.port))

        self.server = MyHTTPServer((self.host, self.port), HttpServerHandler, self.handler)
        self.server.serve_forever()

class Monitor(heart.Heart_Monitor):
    def __init__(self,serial_device="/dev/ttyUSB0"):
        heart.Heart_Monitor.__init__(self,serial_device)
        thread.start_new_thread(self.start,())

    def on_beat(self):
        #self.datafile.write(self.beat_time)
        print(self.beat_time, file=self.datafile)
        print(self.beat_time)

    def start(self):
        now = datetime.datetime.now()
        start_time = now.strftime('%Y-%m-%d-%H:%M:%S')
        self.datafile = open(start_time+".txt","w")
        self.datafile.write("# R wave intervals in milliseconds per line\n")
        self.datafile.write("# Active training\n")
        self.datafile.write("# start time: %s, %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),time.time()))

        while True:
            self.listen_for_beat()

    def json_stats(self):
        std1= round(np.std(self.RR_intervals[-10:]))
        std2= round(np.std(self.RR_intervals[-50:]))
        avg = round(np.average(self.RR_intervals[-7:]))

        return json.dumps({"last":self.beat_time,"std1":std1,"std2":std2,"avg":avg})


if __name__ == "__main__":
    #logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',level=logging.INFO)
    monitor=Monitor()
    server = HttpServer( "localhost", 9999, monitor)
    server.start()
