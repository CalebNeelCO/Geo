#http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
from flask import Flask
import json




def readTags(file='data/Tags.json'):
	rawData = open('data/Tags.json', "r") 
	readData = rawData.read()
	rawData.close()
	data = json.loads(readData)
	return data


def printTags(data=readTags()):
	return json.dumps(data, sort_keys=True, indent=4)


def appendTag(get, userName, file='data/Tags.json'):
	data = readTags()
	if userName in data:
		data[userName].append(get)
	else:
		data[userName] = []  
		data[userName].append(get)
	saveData(data)


def updateTag(tag1, data):
	tmp =  readTags()
	tmp[tag1] = data
	saveData(tmp)


def saveData(data, file='data/Tags.json'):
	f = open(file,'w')
	f.write(str(printTags(data)))	
	f.close()

class geo():
	def __init__(self, tag, descrption, creator, date, found, cache):
 		print ""

 		
	def formatTag():
		data = {}  
		data[tag] = []  
		data[tag].append({  
	    'description': descrption,
	    'creator': 'creator',
	    'date': date,
	    'found': found,
	    'cache': cache
		})
		return data
