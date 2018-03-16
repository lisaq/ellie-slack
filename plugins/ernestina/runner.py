import random
import time

import ernestina

from rtmbot import BOT_SLACK_ID


crontable = []
outputs = []


def process_message(data):
    # Sleep for a bit before replying; you'll seem more real this way
    time.sleep(random.randint(0, 9) * .2)

    if BOT_SLACK_ID in data['text'] or data['channel'].startswith('D'):
        outputs.append(
            [data['channel'], "{}".format(ernestina.respond(data['text']))])
