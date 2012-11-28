#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

to_add = os.path.join(os.path.dirname(__file__), "astral")
sys.path.append(to_add)
to_add = os.path.join(os.path.dirname(__file__), "pytz-2012f")
sys.path.append(to_add)

import oauth
import datetime
import pytz
from astral import *
import moonphase_bot.tokens as tokens

client = oauth.TwitterClient(tokens.application_key, tokens.application_secret, None)
url = 'https://api.twitter.com/1/statuses/update.json'

a = Astral()
city_name = 'Tokyo'
a.solar_depression = 'civil'
city = a[city_name]
timezone = city.timezone

one_day = datetime.timedelta(days=1)
tomorrow = datetime.datetime.now() + one_day

sun = city.sun(date=datetime.datetime.now(), local=True)
sun1 = city.sun(date=tomorrow, local=True)

moonphase = a.moon_phase(datetime.datetime.now(), None)
if moonphase == 0:
  meter = "■■■■■■■■■■■■■■"
elif moonphase == 1:
  meter = "■■■■■■■■■■■■■□"
elif moonphase == 2:
  meter = "■■■■■■■■■■■■□□"
elif moonphase == 3:
  meter = "■■■■■■■■■■■□□□"
elif moonphase == 4:
  meter = "■■■■■■■■■■□□□□"
elif moonphase == 5:
  meter = "■■■■■■■■■□□□□□"
elif moonphase == 6:
  meter = "■■■■■■■■□□□□□□"
elif moonphase == 7:
  meter = "■■■■■■■□□□□□□□"
elif moonphase == 8:
  meter = "■■■■■■□□□□□□□□"
elif moonphase == 9:
  meter = "■■■■■□□□□□□□□□"
elif moonphase == 10:
  meter = "■■■■□□□□□□□□□□"
elif moonphase == 11:
  meter = "■■■□□□□□□□□□□□"
elif moonphase == 12:
  meter = "■■□□□□□□□□□□□□"
elif moonphase == 13:
  meter = "■□□□□□□□□□□□□□"
elif moonphase == 14:
  meter = "□□□□□□□□□□□□□□"
elif moonphase == 15:
  meter = "□□□□□□□□□□□□□■"
elif moonphase == 16:
  meter = "□□□□□□□□□□□□■■"
elif moonphase == 17:
  meter = "□□□□□□□□□□□■■■"
elif moonphase == 18:
  meter = "□□□□□□□□□□■■■■"
elif moonphase == 19:
  meter = "□□□□□□□□□■■■■■"
elif moonphase == 20:
  meter = "□□□□□□□□■■■■■■"
elif moonphase == 21:
  meter = "□□□□□□□■■■■■■■"
elif moonphase == 22:
  meter = "□□□□□□■■■■■■■■"
elif moonphase == 23:
  meter = "□□□□□■■■■■■■■■"
elif moonphase == 24:
  meter = "□□□□■■■■■■■■■■"
elif moonphase == 25:
  meter = "□□□■■■■■■■■■■■"
elif moonphase == 26:
  meter = "□□■■■■■■■■■■■■"
elif moonphase == 27:
  meter = "□■■■■■■■■■■■■■"
elif moonphase == 28:
  meter = "■■■■■■■■■■■■■■"


if moonphase > 29:
  tweet = "うーん。計算できなかったみたい。"
else:
  tweet = 'きょうの月齢は' + str(moonphase) + 'だよ。' + city_name + 'の日没は' + str(sun['sunset'].strftime("%H時%M分%S秒")) + 'くらい、明日の日の出は' + str(sun1['sunrise'].strftime("%H時%M分%S秒")) + 'くらいだよ。' + meter

params = { 'status': tweet }
result = client.make_request(url,
                             token = tokens.user_token,
                             secret = tokens.user_secret,
                             additional_params = params,
                             method = 'POST')

print 'Content-Type: text/plain'
print ''
print result.content