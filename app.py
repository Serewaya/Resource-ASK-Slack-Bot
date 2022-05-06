import os
from pydoc import pager, text
from sunau import Au_read
from tkinter import PAGES
from unicodedata import category
from slack_bolt import App
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import blocks
import functions
import pymongo
from pymongo import MongoClient 
from linkpreview import link_preview
from slack_bolt.adapter.socket_mode import SocketModeHandler

page =1

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
def handle_view_events(ack, body, say, view, client):
    ack()
    global categories
    global expiration
    categories = view['state']['values']['category']['category']['value']
    expiration = view['state']['values']['expiration']['expiration']['selected_date']
    if expiration == "2022-04-20":
        expiration="none"
    categories = categories.split(", ")
    client.views_open(
        trigger_id =body["trigger_id"], 
        view=blocks.personal_information()
    )

@app.view("output_submit_2")
def handle_view_events(ack, body, say, view, client):
    ack()
    user_id = body["user"]['id']
    global area
    global gender
    area = view['state']['values']['area']['static_select-action']['selected_option']['value']
    gender = view['state']['values']['gender']['static_select-action']['selected_option']['value']
    specifics = ", ".join([str(item) for item in categories])
    valid = blocks.user_entry(specifics.title(), expiration.title(), area.title(), gender.title())
    client.chat_postMessage(
        channel=user_id, 
        blocks = valid, 
        text = "Click your messages with the Resource ASK Bot to see more information"
    )

@app.action("dontsearch")
def action_button_click(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        # A simple view payload for a modal
        view=blocks.resource_requirements()
    )
    
@app.action("return_results")
def action_button_click(ack, say, body):
    ack()
    user_id = body["user"]['id']
    values = {"category": { "$in": categories}, "expiration": expiration, "area": area, "gender":gender }
    search = values.copy()
    for value in values:
        if values[value] == "none":
            del search[value]
    results = collection.find(search)
    cat = ", ".join([str(item) for item in categories])
    cat = cat.title()
    count=0
    global listings
    listings = []
    for item in results:
        count+=1
        listings.append(item)
    output = []
    search_location =area.title()
    if search_location == "None":
        search_location="Any Area"
    output.append(blocks.amount(count, search_location, cat))
    output.append(blocks.divider())
    global index
    index =0
    for listing in listings:
        link = listing["link"]
        due = listing["expiration"].title()
        location = listing['area'].title()
        try:
            preview = link_preview(link)
            title = preview.title
            description = preview.description
            description = functions.blurb_format(description)
            image = preview.absolute_image
        except Exception as e:
            title = link
            description = "No description is avalible"
            image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
        if image == None:
            image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
        output.append(blocks.return_listing(link, title, description, image, due))
        output.append(blocks.location(location))
        output.append(blocks.divider())
        index +=1
        if len(listings)>3 and index ==3:
           output.append(blocks.more_listings()) 
           say(blocks=output, text = "Your results")
           break
        elif index == len(listings):
            say(blocks=output, text="Your results")
            index =3
            break
@app.action("more_results")
def action_button_click(ack, say, body):
    ack()
    next_page=[]
    global page
    index = 3*page
    for i in range(3):
        listing = listings[index]
        link = listing["link"]
        due = listing["expiration"].title()
        location = listing['area'].title()
        try:
            preview = link_preview(link)
            title = preview.title
            description = preview.description
            description = functions.blurb_format(description)
            image = preview.absolute_image
        except Exception as e:
            title = link
            description = "No description is avalible"
            image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
        if image == None:
            image = "https://cdn-icons.flaticon.com/png/512/1205/premium/1205916.png?token=exp=1651334128~hmac=71d47b4ca8fb81ca67d34a318a5c2ee5"
        next_page.append(blocks.return_listing(link, title, description, image, due))
        next_page.append(blocks.location(location))
        next_page.append(blocks.divider())
        index +=1
    if index==len(listings):
        say(blocks=next_page, text = "Your results")
    else:
        next_page.append(blocks.more_listings()) 
        say(blocks=next_page, text = "Your results")
    page+=1



@app.command("/output")
def initial(ack, say, command, body):
    user = body['user_name'].title()
    ack()
    elements=blocks.output_initial(user)
    say({"blocks": elements})

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
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()