# guardian-tools

Tools for mucking about with stuff the Guardian produces.

## liveblog2text.py

For example:

	$> bin/liveblog2text.py http://www.theguardian.com/football/2014/jul/05/argentina-v-belgium-world-cup-2014-quarter-final-live | say

Because to this day I can't figure out how to track live blogs via the API...

## liveblog2text-ws.py

Like `liveblog2text.py` except that it wraps all the parsing and stuff in a [simple WebSocket server](https://github.com/opiate/SimpleWebSocketServer). This one doesn't really work so patches and suggestions are definitely welcomed.
