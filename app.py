# import os
# from pydoc import pager, text
# from sunau import Au_read
# from tkinter import PAGES
# from unicodedata import category
# from slack_bolt import App
# from pathlib import Path
# from dotenv import load_dotenv
# from flask import Flask
# import blocks
# import functions
# import pymongo
# from pymongo import MongoClient 
# from linkpreview import link_preview
# import time
# from googlesearch import search
# from search import linksearch
# from search import websearch
# from search import keywords
# from stepinformation import stepchanges

# timeout = 60.0 # Sixty seconds

# page =1
# keyword = 0

# #Main Database
# cluster=MongoClient("mongodb+srv://projectask:wD4odl0AK8ahUmFc@cluster0.e0sdb.mongodb.net/discord?retryWrites=true&w=majority")
# db = cluster["discord"]
# collection = db["id"]

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# # Initializes your app with your bot token and signing secret
# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
# )


# @app.message("verify")
# def ask_for_introduction(event, say):
#     welcome_channel_id = "C03F62GH8N4"
#     user_id = event["user"]
#     text = f"Welcome to the team, <@{user_id}>! 🎉 You can introduce yourself in this channel."
#     say(text=text, channel=welcome_channel_id)
# @app.event("app_home_opened")
# def app_home_opened(event, client, logger):
#     user_id = event["user"]

#     try:
#         # Call the views.publish method using the WebClient passed to listeners
#         result = client.views_publish(
#             user_id=user_id,
#             view=blocks.homepage()
#         )
#         logger.info(result)

#     except SlackApiError as e:
#         logger.error("Error fetching conversations: {}".format(e))

# @app.action("startoutput")
# def action_button_click(ack, body, client):
#     # Acknowledge the shortcut request
#     ack()
#     # Call the views_open method using the built-in WebClient
#     client.views_open(
#         trigger_id=body["trigger_id"],
#         # A simple view payload for a modal
#         view=blocks.resource_requirements()
#     )



# @app.view("output_submit_1")
# def handle_view_events(ack, body, say, view, client):
#     ack()
#     global categories
#     global expiration
#     categories = view['state']['values']['category']['category']['value']
#     expiration = view['state']['values']['expiration']['expiration']['selected_date']
#     if expiration == "2022-04-20":
#         expiration="none"
#     categories = categories.split(", ")
#     client.views_open(
#         trigger_id =body["trigger_id"], 
#         view=blocks.personal_information()
#     )

# @app.view("output_submit_2")
# def handle_view_events(ack, body, say, view, client):
#     ack()
#     user_id = body["user"]['id']
#     global area
#     global gender
#     area = view['state']['values']['area']['static_select-action']['selected_option']['value']
#     gender = view['state']['values']['gender']['static_select-action']['selected_option']['value']
#     specifics = ", ".join([str(item) for item in categories])
#     valid = blocks.user_entry(specifics.title(), expiration.title(), area.title(), gender.title())
#     client.chat_postMessage(
#         channel=user_id, 
#         blocks = valid, 
#         text = "Click your messages with the Resource ASK Bot to see more information"
#     )

# @app.action("dontsearch")
# def action_button_click(ack, body, client):
#     ack()
#     client.views_open(
#         trigger_id=body["trigger_id"],
#         # A simple view payload for a modal
#         view=blocks.resource_requirements()
#     )
    
# @app.action("return_results")
# def action_button_click(ack, say, body):
#     ack()
#     user_id = body["user"]['id']
#     values = {"category": { "$in": categories}, "expiration": expiration, "area": area, "gender":gender }
#     search = values.copy()
#     for value in values:
#         if values[value] == "none":
#             del search[value]
#     results = collection.find(search)
#     cat = ", ".join([str(item) for item in categories])
#     cat = cat.title()
#     count=0
#     global listings
#     listings = []
#     for item in results:
#         count+=1
#         listings.append(item)
#     output = []
#     search_location =area.title()
#     if search_location == "None":
#         search_location="Any Area"
#     output.append(blocks.amount(count, search_location, cat))
#     output.append(blocks.divider())
#     global index
#     index =0
#     for listing in listings:
#         link = listing["link"]
#         due = listing["expiration"].title()
#         location = listing['area'].title()
#         try:
#             preview = link_preview(link)
#             title = preview.title
#             description = preview.description
#             description = functions.blurb_format(description)
#             image = preview.absolute_image
#         except Exception as e:
#             title = link
#             description = "No description is avalible"
#             image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
#         if image == None:
#             image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
#         output.append(blocks.return_listing(link, title, description, image, due))
#         output.append(blocks.location(location))
#         output.append(blocks.divider())
#         index +=1
#         if len(listings)>3 and index ==3:
#            output.append(blocks.more_listings()) 
#            say(blocks=output, text = "Your results")
#            break
#         elif index == len(listings):
#             say(blocks=output, text="Your results")
#             index =3
#             break
# @app.action("more_results")
# def action_button_click(ack, say, body):
#     ack()
#     next_page=[]
#     global page
#     index = 3*page
#     for i in range(3):
#         listing = listings[index]
#         link = listing["link"]
#         due = listing["expiration"].title()
#         location = listing['area'].title()
#         try:
#             preview = link_preview(link)
#             title = preview.title
#             description = preview.description
#             description = functions.blurb_format(description)
#             image = preview.absolute_image
#         except Exception as e:
#             title = link
#             description = "No description is avalible"
#             image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
#         if image == None:
#             image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
#         next_page.append(blocks.return_listing(link, title, description, image, due))
#         next_page.append(blocks.location(location))
#         next_page.append(blocks.divider())
#         index +=1
#     if index==len(listings):
#         say(blocks=next_page, text = "Your results")
#     else:
#         next_page.append(blocks.more_listings()) 
#         say(blocks=next_page, text = "Your results")
#     page+=1



# @app.command("/output")
# def initial(ack, say, command, body):
#     user = body['user_name'].title()
#     ack()
#     elements=blocks.output_initial(user)
#     say({"blocks": elements})

# @app.action("stopoutput")
# def action_button_click(ack, say):
#     ack()
#     say("Sound's great, make sure to call the '/output' slash command when you want to output a resource from the Resource ASK database")

# @app.action("output_resource")
# def action_button_click(body, ack, say, client):
#     ack()
#     user_id = body["user"]['id']
#     client.chat_postMessage(
#         channel=user_id, 
#         blocks = blocks.output_initial(), 
#         text = "Click your messages with the Resource ASK Bot to see more information"
#     )


# if __name__ == "__main__":
#     app.start(host='0.0.0.0',port=3000)
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import string
from datetime import datetime, timedelta
import time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ.get("SLACK_SIGNING_SECRET"), '/slack/events', app)

client = slack.WebClient(token=os.environ.get("SLACK_SIGNING_SECRET"))
BOT_ID = client.api_call("auth.test")['user_id']

message_counts = {}
welcome_messages = {}

BAD_WORDS = ['hmm', 'no', 'tim']

SCHEDULED_MESSAGES = [
    {'text': 'First message', 'post_at': (
        datetime.now() + timedelta(seconds=20)).timestamp(), 'channel': 'C01BXQNT598'},
    {'text': 'Second Message!', 'post_at': (
        datetime.now() + timedelta(seconds=30)).timestamp(), 'channel': 'C01BXQNT598'}
]


class WelcomeMessage:
    START_TEXT = {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Welcome to this awesome channel! \n\n'
                '*Get started by completing the tasks!*'
            )
        }
    }

    DIVIDER = {'type': 'divider'}

    def __init__(self, channel):
        self.channel = channel
        self.icon_emoji = ':robot_face:'
        self.timestamp = ''
        self.completed = False

    def get_message(self):
        return {
            'ts': self.timestamp,
            'channel': self.channel,
            'username': 'Welcome Robot!',
            'icon_emoji': self.icon_emoji,
            'blocks': [
                self.START_TEXT,
                self.DIVIDER,
                self._get_reaction_task()
            ]
        }

    def _get_reaction_task(self):
        checkmark = ':white_check_mark:'
        if not self.completed:
            checkmark = ':white_large_square:'

        text = f'{checkmark} *React to this message!*'

        return {'type': 'section', 'text': {'type': 'mrkdwn', 'text': text}}


def send_welcome_message(channel, user):
    if channel not in welcome_messages:
        welcome_messages[channel] = {}

    if user in welcome_messages[channel]:
        return

    welcome = WelcomeMessage(channel)
    message = welcome.get_message()
    response = client.chat_postMessage(**message)
    welcome.timestamp = response['ts']

    welcome_messages[channel][user] = welcome


def list_scheduled_messages(channel):
    response = client.chat_scheduledMessages_list(channel=channel)
    messages = response.data.get('scheduled_messages')
    ids = []
    for msg in messages:
        ids.append(msg.get('id'))

    return ids


def schedule_messages(messages):
    ids = []
    for msg in messages:
        response = client.chat_scheduleMessage(
            channel=msg['channel'], text=msg['text'], post_at=msg['post_at']).data
        id_ = response.get('scheduled_message_id')
        ids.append(id_)

    return ids


def delete_scheduled_messages(ids, channel):
    for _id in ids:
        try:
            client.chat_deleteScheduledMessage(
                channel=channel, scheduled_message_id=_id)
        except Exception as e:
            print(e)


def check_if_bad_words(message):
    msg = message.lower()
    msg = msg.translate(str.maketrans('', '', string.punctuation))

    return any(word in msg for word in BAD_WORDS)


@ slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if user_id != None and BOT_ID != user_id:
        if user_id in message_counts:
            message_counts[user_id] += 1
        else:
            message_counts[user_id] = 1

        if text.lower() == 'start':
            send_welcome_message(f'@{user_id}', user_id)
        elif check_if_bad_words(text):
            ts = event.get('ts')
            client.chat_postMessage(
                channel=channel_id, thread_ts=ts, text="THAT IS A BAD WORD!")


@ slack_event_adapter.on('reaction_added')
def reaction(payload):
    event = payload.get('event', {})
    channel_id = event.get('item', {}).get('channel')
    user_id = event.get('user')

    if f'@{user_id}' not in welcome_messages:
        return

    welcome = welcome_messages[f'@{user_id}'][user_id]
    welcome.completed = True
    welcome.channel = channel_id
    message = welcome.get_message()
    updated_message = client.chat_update(**message)
    welcome.timestamp = updated_message['ts']


@ app.route('/message-count', methods=['POST'])
def message_count():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    message_count = message_counts.get(user_id, 0)

    client.chat_postMessage(
        channel=channel_id, text=f"Message: {message_count}")
    return Response(), 200


if __name__ == "__main__":
    schedule_messages(SCHEDULED_MESSAGES)
    ids = list_scheduled_messages('C01BXQNT598')
    delete_scheduled_messages(ids, 'C01BXQNT598')
    app.run(debug=True)