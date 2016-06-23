# Twitter Troll bot

Ever wanted to send a tweet to every person who tweeted about "Volk" and "Deutsch" to troll them?
Too lazy to do that by hand?
Too lazy to use the Twitter API?
This script can log into your Twitter account and post a new tweet, all without the official API.

## TODO
...uhhmmm test? I have to admit, i didn't test the whole script, only the every single method.

## System requirements
* Unix like OS (Linux, Mac OS X...)
* curl
* python2

## Instructions
1. apply executable permissions ```chmod +x ./tweet.sh```
2. enter username and password to ```tweet.sh```
3. change the tweet in ```tweet.sh``` (optional)
4. change the twitterfeed/searchfeed in ```t.py``` (optional)
5. usage: ```./t.py```

## Forked from:
* Author: Luka Pusic <luka@pusic.si>
* Github: https://github.com/lukapusic/twitter-bot

## Changelog

#### 15.12.2011
* The script now throws an error if there is no tweet text provided.

### 27.10.2012
* The script is fixed now, fully supports SSL and logouts properly.

### 2.12.2014
* Adjusted the script to twitter changes. Removed --sslv3 curl parameter, changed the way we parse authenticity token. Tested on OSX.

## Known issues
* Sometimes when Twitter updates their website the script stops working, so don't rely on it 100%.

## License
[CC-BY-NC](https://creativecommons.org/licenses/by-nc/2.0/), [Luka Pusic](http://pusic.si)
