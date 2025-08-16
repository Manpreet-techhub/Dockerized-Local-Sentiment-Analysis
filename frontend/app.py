from flask import Flask,render_template, request
import requests
import os
import threading

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
API_URL = "http://backend:8000/analyze"

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    confidence = None
    if request.method == "POST":
        text = request.form["text"]
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(API_URL, json={"text": text}, headers=headers)
        if response.status_code == 200:
            result = response.json()
            sentiment = result["sentiment"]
            confidence = round(result["score"],2)
        else:
            sentiment = f'Error: {response.status_code}'
            confidence = "Could not process the request"
    
    return render_template("index.html", sentiment=sentiment, confidence=confidence)

def openbrowser():
    import webbrowser
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, openbrowser).start()
    app.run(debug=True, host="0.0.0.0",port=5000)







