from flask import Flask
import json


def wrightTags():
	return ""


def appendTag():
	return ""


def updateTag():
	return ""


def saveData(data, file='data/Tags.json'):
	with open(file, 'w') as outfile:  
	    json.dump(data, outfile)


