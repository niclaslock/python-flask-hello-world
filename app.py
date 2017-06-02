from flask import Flask

application = Flask(__name__)

@application.route("/")
def main():
	return "Welcome!"

if __name__ == "__main__":	
	context = ('/secrets/https-private-key/https-public-cert.pem', '/secrets/https-private-key/https-private-key.pem')
	application.run(host='0.0.0.0', port=8080,
	       debug = False, ssl_context=context)
