import slack
import os
from flask import Flask
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

client.chat_postMessage(channel='general', text="Currently sending message after being deployed on heroku :)")
    