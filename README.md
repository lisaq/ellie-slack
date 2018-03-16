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
If you're new to setting up and running and building slackbots,
[this beginner's guide](https://slackhq.com/a-beginner-s-guide-to-your-first-bot-97e5b0b7843d)
is recommended reading.

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

3. Configuration
From the Slack console, you'll get to choose your bot's name and icon.

There's a configuration file called config.conf which is pretty basic; if you're
adding plugins or such which need to be loaded, this is a good place to put them.
It's recommended that you make a second file called local.conf (which is ignored
by github) to set envirnoment variables such as your Slack token.
You'll want to set these:

  ````
  DEBUG: True
  LOGFILE: "logfile.log"
  SLACK_TOKEN: "xoxb-11111111111-222222222222222"
  SLACK_BOT_ID: "UXXXXXXXX"
  ````
Explained:
  `DEBUG`: turn this on locally to get more information on errors
  `LOGFILE`: all the `logging` statements will output here
  `SLACK_TOKEN`: this is the API Token in your bot's settings in the Slack admin interface
  `SLACK_BOT_ID`: your bot's user id can be found in the url when you edit the settings in the admin interface
  note: remove the "B" at the beginning of the id when using it in the configs

4. Run her!

````
  python rtmbot.py
````

### Deployment
You've got to keep her running so long as you'd like her to keep chattering.
We deployed her to Heroku; see [Heroku's Python docs](https://devcenter.heroku.com/articles/getting-started-with-python).
Stuff like the runtime and Procfile are already set up for Heroku.

### Docker
1. If you want to build the Docker image on your own
````
docker build -t napramirez/ellie-slack:1.0 .
````

2. Or if you already have the Slack token and just want to run the Docker image
````
docker run -d --env SLACK_TOKEN="xoxb-11111111111-222222222222222" napramirez/ellie-slack:1.0
````
