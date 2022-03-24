import slack
import os
from pathlib import Path
from flask import Flask
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ["SIGNING_SECRET"],'/slack/events', app)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

if __name__ == "__main__":
    app.run(debug=True)