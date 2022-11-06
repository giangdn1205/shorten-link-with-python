import requests
import random
import json
import sys
import traceback
import urllib


def bomSo(url, custom=""):
	shorten = requests.post('https://bom.so/shorten',
		data = {'url': url,
				'custom': custom,
				'expiry': '',
				'password': '',
				'description': '',
				'multiple': '0'})
	if (shorten.status_code == 200):
		res = json.loads(shorten.text)
		if (res["error"]==0):
			return res["short"].replace(r"\/", "/")
		else:
			return None


def rgl_ink(url, custom=""):
	if (custom==""):
		characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
		custom = ''.join((random.choice(characters) for i in range(random.randint(5,8))))
	shorten = requests.post('https://rgl.ink/',
		data = {'url': url,
				'name_url': custom,
				'submit': ''})
	if (shorten.status_code==200):
		return 'https://rgl.ink/' + custom
	else:
		return None


def hide_URI(url):
	shorten = requests.post('https://hideuri.com/api/v1/shorten',
		data = {'url': url})
	if (shorten.status_code == 200):
		res = json.loads(shorten.text)
		return res["result_url"].replace(r"\/", "/")
	else:
		return None


def ouo_IO(url): # phải vượt link
	shorten = requests.post('https://ouo.io/shorten',
		data = {'url': url})
	if (shorten.status_code == 200):
		res = json.loads(shorten.text)
		if (res["error"]==False):
			return 'https://ouo.io/' + res["slug"]
		else:
			return None


def tinyUrl(url, custom=""): 
	url_link = "http://tinyurl.com/api-create.php?" \
	+ urllib.parse.urlencode({"url": url})
	res = requests.get(url_link)
	if (res.status_code == 200):
		return res.text
	else:
		return None


def vurl_Com(url):
	res = requests.get("https://vurl.com/api.php?url=" + url)
	if (res.status_code==200):
		return res.text
	else:
		return None


link_test = "https://www.youtube.com/watch?v=qzgCB31a458"
custom_test = "2022python5"

# custom
print(bomSo(link_test, custom_test))		# https://bom.so/2022python5
print(rgl_ink(link_test, custom_test))		# https://rgl.ink/2022python5
											
# no custom
print(hide_URI(link_test))			# https://hideuri.com/mGPMRB
print(ouo_IO(link_test))			# https://ouo.io/eX4vvL
print(tinyUrl(link_test))			# https://tinyurl.com/2d2louyb
print(vurl_Com(link_test))			# https://vurl.com/o6wnB
