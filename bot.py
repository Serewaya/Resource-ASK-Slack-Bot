import os
from aiohttp import client
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.main import app

# Initializes your app with your bot token and socket mode handler
app = App(
    token=os.environ.get("SLACK_TOKEN"),
    signing_secret=os.environ.get("SIGNING_SECRET")
)

@client.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")
 
# Start your app
 
if __name__ == "__main__":
        app.run()



    