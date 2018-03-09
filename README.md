# ernestina-slack
Ernestina is a rubber duck who would like to help you with your code.
She currently lives and works at correctiv.org
Her slackbot code is based on Ellie and Eliza.

## Background
Ernestina is a modification of [Ellie](https://github.com/christinac/ellie-slack).
Ellie is a Slack Python-based
[real-time messaging bot](https://github.com/slackhq/python-rtmbot)
wrapped around
Daniel Connelly's [Python implementation](https://github.com/dhconnelly/paip-python)
of Peter Norvig's *Paradigms of AI Programming* Eliza .. with updated diction.

### Modding
If you'd like to dive into Ernestina's innerworkings,
[ernestina.py](https://github.com/lisaq/ernestina-slack/blob/master/plugins/ernestina/ernestina.py)
is your file.

### Dependencies
* [websocket-client](https://pypi.python.org/pypi/websocket-client/)
* [python-slackclient](https://github.com/slackhq/python-slackclient)

### Installation
1. Download Ernestina

  ````
  git clone git@github.com:lisaq/ernestina-slack.git
  cd ernestina-slack
  ````

2. Install dependencies

  ````
  pip install -r requirements.txt
  ````

3. Configure rtmbot ([Slack instructions](https://christinac.slack.com/services/new/bot).)
From the Slack console, you'll get to choose your bot's name and icon.

  ````
  cp example-config/rtmbot.conf .
  vi rtmbot.conf
  SLACK_TOKEN: "xoxb-11111111111-222222222222222"
  ````

4. Run her! (You've got to keep her running so long as you'd like her to keep
chattering; something like [nohup](http://linux.die.net/man/1/nohup) might be helpful.)

````
  python rtmbot.py
````

### Docker
1. If you want to build the Docker image on your own
````
docker build -t napramirez/ellie-slack:1.0 .
````

2. Or if you already have the Slack token and just want to run the Docker image
````
docker run -d --env SLACK_TOKEN="xoxb-11111111111-222222222222222" napramirez/ellie-slack:1.0
````