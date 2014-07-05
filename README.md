# guardian-tools

Tools for mucking about with stuff the Guardian produces.

## liveblog2text.py

For example:

	$> bin/liveblog2text.py http://www.theguardian.com/football/2014/jul/05/argentina-v-belgium-world-cup-2014-quarter-final-live | say

Or:

	$> bin/liveblog2text.py http://www.theguardian.com/football/2014/jul/05/argentina-v-belgium-world-cup-2014-quarter-final-live | slackcat --channel #sportsball

Because to this day I can't figure out how to track live blogs via the [Guardian API](http://www.theguardian.com/open-platform) ...

## liveblog2text-ws.py

Like `liveblog2text.py` except that it wraps all the parsing and stuff in a [simple WebSocket server](https://github.com/opiate/SimpleWebSocketServer). This one doesn't really work so patches and suggestions are definitely welcomed.

I mean it works in that I can connect to the server, once, and have it spew back all the "posts" that have been collected but that's about it. I am not sure how to:

* Set the URL to watch, dynamically
* Run the `watch` thread so that it doesn't block everything else

A close reading of the `SimpleWebSocketServer.py` class would probably be a good place to start...
