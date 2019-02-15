from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
	iot = "Hell KITTY<br><img src=\"https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png\"><br>"
	return iot
