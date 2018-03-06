from flask import Flask
import json
import jworks

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/GetTag", methods=["GET", "POST"])
def error_scribe():

    target_code = flask.request.args.get("input", "")

    return "Hello World!"

if __name__ == "__main__":
    app.run()