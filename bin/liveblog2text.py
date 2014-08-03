#!/usr/bin/env python

import sys
from guardian.liveblog import liveblog

if __name__ == '__main__':

    url = sys.argv[1]

    blog = liveblog(url)

    for item in blog.watch():
        print item.text.encode('utf8')

        
