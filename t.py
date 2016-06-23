#! /usr/env/python

import subprocess
import feedparser
import urllib
import re
import cStringIO
import os
import time

feed = "https://twitter.com/search.rss?q=volk%20deutsch"
database = []
sendnow = []

def start():
	global sendnow
	print "[+] Sending Tweets"
	for name in sendnow:
		befehl = "./tweet.sh " + name
		print name
		p = subprocess.Popen(befehl, shell=True, bufsize=0, stdout=subprocess.PIPE)
		p.wait()

def scrape():
	global database
	print "[+] Reading feed"
	response = urllib.urlopen(feed)
	html = response.read()
	#data-screen-name="!!!!! " data-name="
	suchlist = []
	mup = cStringIO.StringIO(html)
	length = len(mup.read())
	print "[+] Handling data"
	while length != 0:
		mup.seek(length)
		map = mup.readline()
		suchlist.append(map)
		length = length - 1
	print "[+] Searching usernames"
	start = "data-screen-name=\""
	end = "\" data-name=\""
	for line in suchlist:
		if re.search(start, line):
			if re.search(end, line): 
				user = (line.split(start))[1].split(end)[0]
				if user not in database:
					database.append(user)
	puttofile()

def puttofile():
	global database
	global sendnow
	send = []
	print "[+] Syncing with database"
	if not os.path.exists('database.txt'):
		open('database.txt', 'w').close()
	f = open("database.txt", "r+a")
	stuff =  f.readlines()
	lol = stuff
	if len(stuff) == 0:
		stuff = stuff + database
		send = database
	else:
		lol[-1] =  lol[-1] + "\n"
		for user in database:
			if user in lol:
				send.append(user)
	send = map(str.strip, send)
	sendnow = send
	send = "\n".join(send)
	f.write(send)
	f.close()
	print send
	start()

def loop():
	while(1 == 1):
		scrape()
                wait = 300  # seconds how long the bot will wait until the next cr4wl
                print "[+] Waiting for " + str(wait/60) + " minutes."
                print
		time.sleep(wait)
		
loop()
# start()
