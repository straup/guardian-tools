#!/usr/bin/env python

import sys
import time
import requests
import BeautifulSoup

class liveblog:

    def __init__(self, url, interval=60):
        self.url = url
        self.seen = []
        self.interval = interval

    def watch(self):

        while True:

            try:
                rsp = requests.get(self.url)

                if not rsp.ok:
                    raise Exception, rsp.reason

                soup = BeautifulSoup.BeautifulSoup(rsp.text)    

                blocks = soup.findAll('div', {'class': 'block'})

                readme = []

                for b in blocks:

                    id = b['id']
                    
                    if id in self.seen:
                        continue

                    el = b.find('div', {'class': 'block-elements'})
                    paras = el.findAll('p')

                    for p in paras:
                        readme.append(p)

                    self.seen.append(id)

                readme.reverse()

                for p in readme:
                    yield p

            except Exception, e:                
                sys.stderr.write("Folied because, %s" % e)

            time.sleep(self.interval)

if __name__ == '__main__':

    url = sys.argv[1]

    b = liveblog(url)

    for txt in b.watch():
        print txt.text.encode('utf8')

        
