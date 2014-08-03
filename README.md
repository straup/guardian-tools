# guardian-tools

Tools for mucking about with stuff the Guardian produces.

## liveblog2text.py

For example:

	$> bin/liveblog2text.py http://www.theguardian.com/football/2014/jul/05/argentina-v-belgium-world-cup-2014-quarter-final-live | say

Or:

	$> bin/liveblog2text.py http://www.theguardian.com/football/2014/jul/05/argentina-v-belgium-world-cup-2014-quarter-final-live | slackcat --channel #sportsball

Because to this day I can't figure out how to track live blogs via the [Guardian API](http://www.theguardian.com/open-platform) ...
