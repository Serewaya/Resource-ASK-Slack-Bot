
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/slack/events")
def home_view():
        return "<h1>Currently Running :)</h1>"