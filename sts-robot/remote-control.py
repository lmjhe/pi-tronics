#!/usr/bin/env python

import pibrella
import time
import BaseHTTPServer


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
#        s.wfile.write("test")
#        print s.path

        if s.path != "/":
            if s.path == "/test.jpg":
                f = open('test.jpg', 'rb')
                s.send_response(200)
                s.send_header("Content-type", "image/jpg")
                s.end_headers()
                s.wfile.write(f.read())
                return
            elif s.path == "/test.html":
                s.send_response(200)
                s.end_headers()
                s.wfile.write('<html><head><meta http-equiv="refresh" content="2"></head><body><p align="center"><img src="/test.jpg" width="640" height="480"></p></body></html>')
                return

            # forward for a short period
            elif s.path == "/forward":
                pibrella.output.on()
                time.sleep(0.5)
                pibrella.output.off()

            # turn for a short period
            elif s.path == "/left":
                pibrella.output.f.on()
                time.sleep(0.5)
                pibrella.output.f.off()
            elif s.path == "/right":
                pibrella.output.e.on()
                time.sleep(0.5)
                pibrella.output.e.off()

            # forward indefinetely
            elif s.path == "/forwardstart":
                pibrella.output.on()
            elif s.path == "/forwardstop":
                pibrella.output.off()

            # turn indefinetely
            elif s.path == "/leftstart":
                pibrella.output.f.on()
            elif s.path == "/rightstart":
                pibrella.output.e.on()
            elif s.path == "/leftstop":
                pibrella.output.f.off()
            elif s.path == "/rightstop":
                pibrella.output.e.off()
            s.send_response(200)
            s.end_headers()
            s.wfile.write("done");
            return

#       otherwise s.path == "/"...
        s.send_response(200)
        s.end_headers()
        s.wfile.write('<html><head><style>a { font-size: large; color: black; border: 3px solid black; padding: 1em; } p { padding: 3px; margin-top: 2.5em; }</style></head>\n')
        s.wfile.write('<body><h1 align="center">A simple, open robot</h1>\n')

        s.wfile.write('<p align="center"><a href="/forward" target="myframe">forward</a> ')
        s.wfile.write('<a href="/left" target="myframe">left</a> ')
        s.wfile.write('<a href="/right" target="myframe">right</a></p>\n')

        s.wfile.write('<p align="center"><a href="/forwardstart" target="myframe">forwardstart</a> ')
        s.wfile.write('<a href="/forwardstop" target="myframe">forwardstop</a></p>\n')

        s.wfile.write('<p align="center"><a href="/leftstart" target="myframe">leftstart</a> ')
        s.wfile.write('<a href="/leftstop" target="myframe">leftstop</a></p>\n')

        s.wfile.write('<p align="center"><a href="/rightstart" target="myframe">rightstart</a> ')
        s.wfile.write('<a href="/rightstop" target="myframe">rightstop</a></p>\n')

#        s.wfile.write('<p><br/><p align="center"><iframe src="/test.html" width="680" height="520"></iframe></p>')
        s.wfile.write('<iframe src="/" name="myframe" style="display: none">\n')
        s.wfile.write('</body></html>\n')


server_class=BaseHTTPServer.HTTPServer
httpd=server_class(("0.0.0.0", 80), MyHandler)
httpd.serve_forever()

