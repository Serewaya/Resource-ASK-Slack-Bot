
from flask import Flask
 
client = Flask(__name__)
 
@client.route("/")
def home_view():
        return "<h1>Currently Running :)</h1>"