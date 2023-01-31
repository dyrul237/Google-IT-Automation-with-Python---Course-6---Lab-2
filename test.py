#! /usr/bin/env python3


import os
import requests

keys = ["title", "name", "date", "feedback"]		# key values for directory
source = '/home/kali/gia_course6_lab2/feedback/' 	# where you put the directory of feedback
url = "http://localhost/feedback/"			# host url
feedback_to_post = []


files = os.listdir(source)
#print (files)						# to check the output of list of files


def iteration(x):					# will iterate each line in a file
	with open (source+ x ) as f:			# will open the file
		line_files = f.read().splitlines()	# will read all the contents of the file then 
	return line_files				# the splitlines() method splits the lines into a 								# list. The splitting is done at line breaks. then 								# return the value to line_files
	

for x in files:						# will iterate each file in the directory
	line_files = iteration(x)			# will pass the file to function(iteration) with x parameter
	feedback_to_post.append(dict(zip(keys, line_files)))
	

for entry in feedback_to_post:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")

	

	
	


