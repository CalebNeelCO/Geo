from flask import Flask
import json
import jworks




yes = {}
yes = {  
    'Tag': 'abc',
    'Value': 'asfasdf',
    'Times called': 'Nebraska'
}
jworks.appendTag(yes)

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

	