from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
	return "Welcome!"

if __name__ == "__main__":
	context = ('https-ca-certificates.pem', 'https-private-key.pem')
	app.run(host='0.0.0.0', port=8080,
	       debug = False, ssl_context=context)
