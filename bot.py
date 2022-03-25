import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from keep_alive import keep_alive


# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_SECRET"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html///
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")
 
# Start your app
keep_alive()


    