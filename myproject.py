from flask import Flask

application = Flask(__name__)

@application.route("/")
def main():
	return "Welcome!"

if __name__ == "__main__":
	application.run(host='0.0.0.0')
	
#	context = ('https-public-cert.pem', 'https-private-key.pem')
#	app.run(host='0.0.0.0', port=8080,
#	       debug = False, ssl_context=context)
