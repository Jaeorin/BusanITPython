#-*- coding: utf-8 -*-
from bottle import get, post, request, template, run
try:
	from urllib.request import urlopen #python 3
except ImportError:
	from urllib2 import urlopen #python 2

deviceIP = "192.168.0.75"
portnum = "80"

base_url = "http://" + deviceIP + ":" + portnum
led_url = base_url + "/led"
events_url = base_url + "/events"

@post('/led')
def controlled():
	print "controlled"
	l = request.body.read()
	print l
	if l == "ON":
		print "2"
		print led_url
		u = urlopen(led_url, "on")
		print "3"
	elif l == "OFF":
		print "4"
		print led_url
		u = urlopen(led_url, "off")
		print "5"

@get('/events')
def getevents():
	print "events"
	u = urlopen(events_url)
	data = ""
	try:
		data = u.read()
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]
	return data	

@get('/')
def index():
	print "index"
	return template("index")

@get('/dhtchart')
def dht22chart():
	print "dhtchart"
	return template("dhtchart")

if __name__ == '__main__':
	print "server running"
	run(host="192.168.0.210", port=8020)	
