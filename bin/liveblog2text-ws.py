#!/usr/bin/env python

import sys
import time
import requests
import BeautifulSoup

from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

class blog(WebSocket):

    def __init__(self, server, sock, address):
        WebSocket.__init__(self, server, sock, address)

        url = 'http://www.theguardian.com/football/2014/jul/05/argentina-v-belgium-world-cup-2014-quarter-final-live'
        self.watch(url)

    def handleMessage(self):
        if self.data is None:
            self.data = ''
            
        self.sendMessage(str(self.data))

    def handleConnected(self):
        print "connected"

    def handleClose(self):
        pass
    
    def watch(self, url):
        
        seen = []
            
        while True:

            try:
                rsp = requests.get(url)

                if not rsp.ok:
                    raise Exception, rsp.reason

                soup = BeautifulSoup.BeautifulSoup(rsp.text)    

                blocks = soup.findAll('div', {'class': 'block'})

                for b in blocks:

                    id = b['id']
                    
                    if id in seen:
                        continue

                    el = b.find('div', {'class': 'block-elements'})
                    paras = el.findAll('p')

                    for p in paras:
                        self.sendMessage(str(p.text))

                    seen.append(id)

            except Exception, e:                
                sys.stderr.write("Folied because, %s" % e)

            time.sleep(60)

if __name__ == '__main__':

    url = sys.argv[1]

    server = SimpleWebSocketServer('', 8000, blog)
    server.serveforever()

