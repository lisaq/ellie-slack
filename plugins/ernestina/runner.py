import os
import random
import time

import ernestina

import yaml


crontable = []
outputs = []
config = yaml.load(file('rtmbot.conf', 'r'))
bot_id = os.getenv("BOT_SLACK_ID", config["BOT_SLACK_ID"])


def process_message(data):
    if bot_id in data['text'] or data['channel'].startswith('D'):
        # Sleep for a bit before replying; you'll seem more real this way
        time.sleep(random.randint(0, 9) * .2)
        outputs.append(
            [data['channel'], "{}".format(ernestina.respond(data['text']))])
