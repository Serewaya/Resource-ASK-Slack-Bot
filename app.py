import os
from pydoc import text
from unicodedata import category
from slack_bolt import App
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import blocks
import functions
import pymongo
from pymongo import MongoClient 

cluster=MongoClient("mongodb+srv://projectask:wD4odl0AK8ahUmFc@cluster0.e0sdb.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["id"]

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
@app.event("app_home_opened")
def app_home_opened(event, client, logger):
    user_id = event["user"]

    try:
        # Call the views.publish method using the WebClient passed to listeners
        result = client.views_publish(
            user_id=user_id,
            view=blocks.homepage()
        )
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error fetching conversations: {}".format(e))

@app.action("startoutput")
def action_button_click(ack, body, client):
    # Acknowledge the shortcut request
    ack()
    # Call the views_open method using the built-in WebClient
    client.views_open(
        trigger_id=body["trigger_id"],
        # A simple view payload for a modal
        view=blocks.resource_requirements()
    )



@app.view("output_submit_1")
def handle_view_events(ack, body, say, view):
    ack()
    value1 = view['state']['values']['category']['category']['value']
    value2 = view['state']['values']['expiration']['expiration']['selected_date']
    print(value1)
    print(value2)

@app.command("/output")
def initial(ack, say, command, body):
    user = body['user_name'].title()
    ack()
    elements=blocks.output_initial(user)
    say({"blocks": elements})

# @app.action("startoutput")
# def action_button_click(ack, say):
#     ack()
#     say(blocks.output_instructions())
#     @app.event("message")
#     def handle_message_events(body, message, say):
#         content = str(message["text"])
#         global indices
#         indices = content.split(", ")
#         if len(indices) != 5:
#             say("*Please enter in the form of:* _link, category, expiration time, area, gender_")
#             @app.event("message")
#             def handle_message_events(body, message, say):
#                 content = message["text"]
#                 indices = content.split(", ")
#         if len(indices) ==5:
#             indices = [x.lower() for x in indices]
#             link, section, expiration, area, gender = indices
#             say(blocks.user_entry(link, section, expiration, area, gender))

# @app.action("return_results")
# def action_button_click(ack, say):
#     ack()
#     results = functions.return_database(indices)
#     for i in results:
#         say(i['link'])


@app.action("stopoutput")
def action_button_click(ack, say):
    ack()
    say("Sound's great, make sure to call the '/output' slash command when you want to output a resource from the Resource ASK database")

@app.action("output_resource")
def action_button_click(body, ack, say, client):
    ack()
    user_id = body["user"]['id']
    client.chat_postMessage(
        channel=user_id, 
        blocks = blocks.output_initial(), 
        text = "Click your messages with the Resource ASK Bot to see more information"
    )


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))