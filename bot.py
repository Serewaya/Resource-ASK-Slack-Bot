import slack
import os
from pathlib import Path


client = slack.WebClient(token=os.environ[SLACK_TOKEN])