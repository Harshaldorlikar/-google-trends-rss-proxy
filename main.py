from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/rss")
def rss():
    geo = request.args.get("geo", "US")
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={geo}"
    response = requests.get(url)
    return Response(response.content, mimetype='application/xml')

@app.route("/")
def home():
    return "✅ Google Trends RSS Proxy is working!"
