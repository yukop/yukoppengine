#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oauth
import datetime
import geeklatte_bot.tokens as tokens

client = oauth.TwitterClient(tokens.application_key, tokens.application_secret, None)
url = 'https://api.twitter.com/1/statuses/update.json'

import urllib2
import json
import random
import re

data = urllib2.urlopen('http://geeklatte.com/geeklatte_all.json')
dictFromJson = json.load(data)
photoset = dictFromJson['photoset']
ownername = photoset['ownername']
setid = photoset['id']
photos = photoset['photo']

n = random.randrange(len(photos))
photo = photos[n]
id = photo['id']
photo_url = 'http://www.flickr.com/photos/' + ownername + '/' + id + '/in/set-' + setid + '/'

tweet = photo['title'] + ' ' + photo_url + ' (' + re.sub('\s\d\d:\d\d:\d\d', '', photo['datetaken']) + ') #geeklatte'

params = { 'status': tweet }
result = client.make_request(url,
                             token = tokens.user_token,
                             secret = tokens.user_secret,
                             additional_params = params,
                             method = 'POST')

print 'Content-Type: text/plain'
print ''
print result.content