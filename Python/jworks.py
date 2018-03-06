
from flask import Flask
import json


def wrightTags():
	return ""


def readTags(file='data/Tags.json'):
	rawData = open('data/Tags.json', "r") 
	readData = rawData.read()
	data = json.loads(readData)
	return data

def appendTag(get, userName, file='data/Tags.json'):
	data = readTags()
	if userName in data:
		data[userName].append(get)
	else:
		data[userName] = []  
		data[userName].append(get)
	saveData(data, file='data/Tags.json')


def updateTag():
	return ""


def saveData(data, file='data/Tags.json'):
	with open(file, 'w') as outfile:  
	    json.dump(data, outfile)


