#!/usr/bin/env python

import sys
import redis
import json
from guardian.liveblog import liveblog

if __name__ == '__main__':

    # TO DO: proper CLI arguments

    url = sys.argv[1]
    channel = sys.argv[2]

    blog = liveblog(url)

    ps = redis.Redis()
    
    for item in blog.watch():

        txt = item.text.encode('utf8')
        data = json.dumps({'text': txt})

        ps.publish(channel, data)
