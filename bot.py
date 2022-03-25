import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.main import app

# Initializes your app with your bot token and signing secret
client = App(
    token=os.environ.get("SLACK_TOKEN"),
    signing_secret=os.environ.get("SIGNING_SECRET")
)

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@client.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

 
if __name__ == "__main__":
        app.run()



    