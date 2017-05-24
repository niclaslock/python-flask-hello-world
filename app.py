from flask import Flask
import SSL

app = Flask(__name__)
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('https-private-key.pem')
context.use_certificate_file('https-public-cert.pem')

@app.route("/")
def main():
	return "Welcome!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080,
	       debug = False/True, ssl_context=context)
