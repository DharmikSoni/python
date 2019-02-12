#!/usr/bin/python3

from logWatcher import LogWatcher
#import json
import requests
import os
import pymysql
import glob

# getting only updated entry : logWatcher.py(module)
class Updated_Log:
	def callback(filename, lines):
		for log in lines:
			print(log)
			#sending data in json format to api/
			# data='{\
	  #   		"meta": {\
	  #       		"clientID": "34",\
	  #       		"authToken": "da0d4b897b1cb4ef6b381531692fdefc7f107b15109feda4bb9960a018869f7f9323846ed9bd81add87dc244f86b228047d3abf5052d679bd54ac4a4d433b107n+jhxyP22SwmTGHKXn79iO6lAhZjNH1q9g==",\
	  #       		"os": "ubuntu",\
	  #       		"ip": "192.168.1.158",\
	  #       		"version": "1.0.0",\
	  #       		"timestamp": "Fri Nov  2 18:12:45 2018"\
	  #   		},\
	  #   			"logType": "syslog",\
	  #   			"logDetails": "{log}"\
			# }'
			# data_json = json.loads(data)
			# payload=json.dumps(data_json, indent=2, sort_keys=True)
			# # print(payload)
			# payload_json={'json_payload':payload}
			# r=requests.post('http://localhost/watch7_ui/benchmarking/validate_get/', data=payload) #meta information
			# print(r.headers)

if __name__ == "__main__":
	#watcher=LogWatcher("/home/zerocool/Desktop/cpanel1/epiz_23204936",Updated_Log.callback,tail_lines=1)
	watcher=LogWatcher("/var/log/",Updated_Log.callback,tail_lines=1)
	watcher.loop() #checking at interval of 0.01 seconds

			
# problem1 : program checks for only new line if found then shown. but if file manually modified in existing entry on server then no line shown updated.
# solution
# if(newline) then
# callback
# else(select from ftpd modtime)
# 	if(change in modtime) then
# 		callback

#problem2 : how to send multiple logType along with logDetails(syslog,apache,mysql,nginx)
#problem3 : how will identify which logDetails->logType when passed.

# downloading
# preserve timestamp
# store info of file in database
# compare with modified time of previous file and again update in database, but it updates every file again when program run
# send only last logs to loganalyzer-> sent meta info and log from callback
# multiple ftp users
# set cron job->ftp runs every 10 second, downloads files->store info in database, send log files to logWatcher->send meta and log to loganalyzer