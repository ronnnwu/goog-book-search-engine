from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("hello.html")

@app.route("/search", methods=["POST", "GET"])
def search(): 
    if request.method == "POST":
        url = "https://www.googleapis.com/books/v1/volumes?q=" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return render_template("results.html", api_data=response_dict)
    else: # request.method == "GET"
        return render_template("search.html")
    	


if __name__ == "__main__":
    app.run(host="0.0.0.0")	