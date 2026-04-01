from flask import Flask

app = Flask(__name__)

@app.route("/")
def docker_image():
    return "<p>This is my first image</p>"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
