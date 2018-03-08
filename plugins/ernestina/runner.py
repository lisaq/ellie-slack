import random
import time

import ernestina

crontable = []
outputs = []


def process_message(data):
    # Sleep for a bit before replying; you'll seem more real this way
    time.sleep(random.randint(0, 9) * .2)
    outputs.append(
        [data['channel'], "{}".format(ernestina.respond(data['text']))])
