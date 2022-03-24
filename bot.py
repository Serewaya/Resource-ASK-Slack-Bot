import slack
import os
from flask import Flask

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

client.chat_postMessage(channel='general', text="Currently sending message after being deployed on heroku :)")
    