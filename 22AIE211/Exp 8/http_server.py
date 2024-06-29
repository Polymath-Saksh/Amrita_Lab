from flask import Flask
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def hello_http():
	return "Hello HTTP!"

if __name__ == '__main__':
    app.run(debug = True)