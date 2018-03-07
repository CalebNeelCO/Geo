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


def appendTag(get, userName, tag, file='data/Tags.json'):

	data = readTags(file)
	if(userName in data):
		#if( in data[userName])
		print data[userName][0]['uid']
		data[userName].append(get)
	else:
		data[userName] = []
		data[userName].append(get)
	saveData(data)


def updateTag(tag1, data): #needs work
	tmp =  readTags()
	tmp[tag1] = data
	saveData(tmp)


def saveData(data, file='data/Tags.json'):
	f = open(file,'w')
	f.write(str(printTags(data)))	
	f.close()

def tagToClass(user, tag, data):
	return geo(tag, data[0]['description'], user, data[0]['date'], data[0]['found'], data[0]['cache'], data[0]['uid'])

def Gettag(user, tag, data=readTags()):
	return data[user][0][tag]

def newUid():
	high = 0;
	data = readTags()
	for p in data:
		x = data[p][0]
		for i in x:
			h = data[p][0][i][0]['uid']
			if(h > high):
				high = h
	return high + 1

			

class geo:
	def __init__(self,tag, descrption, creator, date, found, cache, uid):
		self.tag = tag
		self.descrption = descrption
		self.creator = creator
		self.date = date
		self.found = found
		self.cache = cache
		self.uid = uid
	def formatTag(self):
		data = {}
		data[self.tag] = []  
		data[self.tag].append({
		'description': self.descrption,
		'creator': self.creator,
		'date': self.date,
		'found': self.found,
		'cache': self.cache,
		'uid': self.uid
		})
		return data
	def save(self):
		appendTag(self.formatTag(), "tip1", "tag") #fix this
	def tag(self):
		return self.tag
	def descrption(self):
		return self.descrption
	def creator(self):
		return self.creator
	def date(self):
		return self.date
	def found(self):
		return self.found
	def cache(self):
		return self.cache
	def uid(self):
		return self.uid
	
	


	