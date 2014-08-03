#!/usr/bin/env python

import sys
import redis
from guardian.liveblog import liveblog

if __name__ == '__main__':

    # TO DO: proper CLI arguments

    url = sys.argv[1]
    channel = sys.argv[2]

    blog = liveblog(url)

    ps = redis.Redis()
    
    for item in blog.watch():
        txt = item.text.encode('utf8')
        ps.publish(channel, txt)
