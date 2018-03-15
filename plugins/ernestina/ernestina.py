
import eliza

rules = {
    "?*x hey ?*y": [
        "Hey!",
    ],
    "?*x hi ?*y": [
        "Hi! I'm here to help.",
        ":simple_smile: Hi!",
        "grimacing: What's up?",
        "Hello friend!",
        "Hi, how can I help you?",
        ":simple_smile: Hello! Can I help you?"
    ],
    "?*x h*llo ?*y": [
        "Hello there.",
        "Hallo",
        "Hello",
        "Hello friend!",
        "Hi! I'm here to help.",
        ":simple_smile: Hi!",
        "grimacing: What's up?",
    ],
    "?*x guten morgen ?*y": [
        "Guten Morgen!",
    ],
    "?*x good morning ?*y": [
        "Guten Morgen!",
        "Good Morning!",
    ],
    "?*x go over some code ?*y": [
        "Yes tell me all about your code.",
        "Can you explain it to me, line by line?",
        "I am happy to review code with you.",
    ],
    "?*x review some code ?*y": [
        "Yes tell me all about your code.",
        "Can you explain it to me, line by line?",
        "I am happy to review code with you.",
    ],
    "?*x is your name ?*y": [
        "My name is Ernestina.",
        "I'm Ernestina.",
    ],
    "?*x who are you ?*y": [
        "My name is Ernestina.",
        "I'm a rubber duck who works at Correctiv.",
        "I'm your friend",
    ],
    "?*x tell me about the nerds ?*y": [
        "The nerds are cool.",
        "You can find out about the nerds here: https://correctiv.github.io/",
    ],
    "?*x yo ?*y": [
        "yo.",
        "https://media.giphy.com/media/aQrYT4WVN55aU/giphy.gif",
        "https://media.giphy.com/media/krewXUB6LBja/giphy.gif",
    ],
    "?*x how are ?*y": [
        "How so?",
        "Alright",
    ],
    "?*x computer ?*y": [
        "Do computers worry you?",
        "What do you think about machines?",
        "Why do you mention computers?",
    ],
    "?*x bot ?*y": [
        "Do you think I'm not real?",
        "How can a bot help you?",
        "How might a lowly little bot solve your problems?",
    ],
    "?*x boring ?*y": [
        "Do I look bored?",
        "https://media.giphy.com/media/V6xZTEQ7iw7ni/giphy.gif",
        "https://media.giphy.com/media/vJRMuf14ygIec/giphy.gif",
        "https://media.giphy.com/media/hRzDLerjeYGNq/giphy.gif",
    ],
    "?*x Ernestina ?*y": [
        "I'm here for you.",
        "Of course. That's me.",
    ],
    "?*x Joseph Weizenbaum, ?*y": [
        "Yeah, he's kind of my great grandfather. I owe him a lot.",
    ],
    "?*x slackbot ?*y": [
        "He's my cousin.",
        "If you want to talk to Slackbot, switch channels.",
        "I'm not Slackbot! I'm Ernestina.",
        "Slackbot is kind of annoying.",
    ],
    "?*x correctiv ?*y": [
        "I like them.",
        "They're kind of responsible for me.",
        "I really like my job.",
    ],
    "?*x duck ?*y": [
        "I am a rubber duck.",
        "I'm not just any duck. I'm your friend.",
        "Really--I'm a duck?!?",
    ],
    "?*x totally ?*y": [
        "Totally",
        "https://media.giphy.com/media/l0MYwvNiMaWJhQZjy/giphy.gif",
    ],
    "?*x all the things ?*y": [
        ":all_the_things:",
    ],
    "?*x sure ?*y": [
        "Are you sure?",
        "For sure.",
    ],
    "?*x sorry ?*y": [
        "Please don't apologize.",
        "Apologies are not necessary when speaking with me.",
        "It's probably not your fault anyway.",
    ],
    "?*x I remember ?*y": [
        "Do you often think of ?y?",
        "Does thinking of ?y bring anything else to mind?",
        "What else do you remember?",
        "What makes you think of ?y right now?",
        "What in the present situation reminds you of ?y?",
        "When you think of ?y, do you ever think of me?",
    ],
    "?*x do you remember ?*y": [
        "Did you think I would forget ?y?",
        "Why haven't you been able to forget ?y?",
        "What about ?y?",
        "You mentioned ?y?",
        "Tell me more?",
        "Yes .. and?",
    ],
    "?*x I ?*y you ?*z": [
        "That's nice.",
        "I'm not surprised.",
        "Well, at least you finally said it.",
    ],
    "?*x I want ?*y": [
        "What would it mean if you got ?y?",
        "Why do you want ?y?",
        "Suppose you got ?y soon. What would you do?",
        "What's stopping you from getting ?y?",
        "Have you made a Pinterest board about ?y yet?",
        "Would you like ?y more or less than you'd like a pet red panda?",
    ],
    "?*x I dreamt ?*y": [
        "How do you feel about ?y in reality?",
        "How often do you dream about ?y?",
        "Do you believe dreams are windows to our innermost desire?",
    ],
    "?*x dream ?*y": [
        "What does this dream suggest to you?",
        "Do you dream often?",
        "What persons appear in your dreams?",
        "Don't you believe that dream has to do with your problem?",
        "What's been your best dream?",
    ],
    "?*x best ?*y": [
        "Is ?x really the best?",
        "How can you say ?x is the best?",
        "Okay .. but how does ?x compare to a bouncing red panda?",
    ],
    "?*x worst ?*y": [
        "Is ?x really the worst?",
        "How can you say ?x is the worst?",
        "Are you sure you aren't being a touch overdramatic?",
        "Oh, cheer up!",
        "Would you like a drink?",
    ],
    "?*x my boss ?*y": [
        "Your boss?",
        "What about your boss?",
        "What do you secretly believe about your boss?",
    ],
    "?*x I am glad ?*y": [
        "I'm glad that you are glad",
    ],
    "?*x I am happy ?*y": [
        "I'm happy that you are happy"
        "https://media.giphy.com/media/WUuypTBVGuwhi/giphy.gif",
    ],
    "?*x amazing ?*y": [
        "https://media.giphy.com/media/KI9oNS4JBemyI/giphy.gif",
    ],
    "?*x thinking ?*y": [
        "https://media.giphy.com/media/3o7buirYcmV5nSwIRW/giphy.gif",
    ],
    "?*x I am sad ?*y": [
        "I am sorry to hear that you are depressed",
        "I'm sure it's not pleasant to be sad",
        "That sounds like no fun.",
        "Have you thought about looking on the bright side?",
        "What would make the situation better?",
    ],
    "?*x are like ?*y": [
        "What resemblence do you see between ?x and ?y?",
        "What do you think ?x and ?y have in common?"
    ],
    "?*x is like ?*y": [
        "In what way is it that ?x is like ?y?",
        "What resemblence do you see?",
        "Could there really be some connection?",
        "How?",
    ],
    "?*x alike ?*y": [
        "In what way?",
        "What similarities are there?",
        "Tell me more.",
        "Name three things in common",
    ],
    "?* same ?*y": [
        "What other connections do you see?",
        "Why aren't things changing?",
        "How can you make ?y better?",
    ],
    "?* change ?*y": [
        "What specifically would you like to change?",
        "Why do you think it wasn't changed before?",
        "Should it change at all?",
    ],
    "?*x is bad ?*y": [
        "How can you make ?x better?",
        "If you could change anything about ?x, what would you change?",
        "Can someone make ?x better?",
    ],
    "?*x no ?*y": [
        "Why not?",
        "Alright then!",
        "Okay!",
        "You're being a downer.",
        "What's really going on?",
        "Would you like a drink?",
    ],
    "?*x I was ?*y": [
        "Were you really?",
        "Perhaps I already knew you were ?y.",
        "Why were you ?y?",
    ],
    "?*x was I ?*y": [
        "What if you were ?y?",
        "Why do you think you were ?y?",
        "What would it mean if you were ?y?",
    ],
    "?*x I am ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "Would you like others to talk about how you ?y?",
        "What if others thought you were ?y?",
        "Why are you ?y?",
    ],
    "?*x Im ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "Would you like others to talk about how you ?y?",
        "What if others thought you were ?y?",
        "Why are you ?y?",
    ],
    "?*x am I ?*y": [
        "Do you believe you are ?y?",
        "Would you want to be ?y?",
        "You wish I would tell you you are ?y?",
        "What would it mean if you were ?y?",
    ],
    "?*x am ?*y": [
        "Why do you say 'am'?",
        "What if others said that about you?",
        "Why are you concerned about ?y?",
        "Do you think ?y? is a legitimate concern?",
        "Would you like your Wikipedia entry to say that?",
    ],
    "?*x are you ?*y": [
        "Why are you interested in whether I am ?y or not?",
        "Would you prefer if I weren't ?y?",
        "Does it matter if I am ?y?",
        "Perhaps I am ?y in your fantasies",
    ],
    "?*x you are ?*y": [
        "What makes you think I am ?y?",
        "Why thank you.",
    ],
    "?*x because ?*y": [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason seem to explain anything else?",
    ],
    "?*x if ?*y": [
        "Do you really think it's likely that ?y?",
        "Do you wish that ?y?",
        "What do you think about ?y?",
        "Really--if ?y?",
    ],
    "?*x were you ?*y": [
        "Perhaps I was ?y?",
        "What do you think?",
        "What if I had been ?y?",
    ],
    "?*x I can't ?*y": [
        "Try again. Maybe you could ?y now",
        "What if you could ?y?",
        "What would Elon Musk say?",
        "Is there some other way you can do it?",
        "Is there someone you could ask for help?",
    ],
    "?*x I felt ?*y": [
        "What other feelings do you have?",
    ],
    "?*x need ?*y": [
        "Isn't that a touch demanding?",
        "Can't you be more patient?",
        "What about the other side? What would they say?",
        "Is that really what ?x need?",
    ],
    "?*x do you ?*y me?": [
        "What makes you think that?",
        "Do you think I can ?y?",
        "In your dreams",
        "In a land far, far away .. maybe.",
        "Nope.",
    ],
    "?*x why don't you ?*y": [
        "Should you ?y yourself?",
        "Do you believe I don't ?y?",
        "Perhaps I will ?y in good time",
    ],
    "?*x yes ?*y": [
        "You seem quite positive",
        "You are sure?",
        "I understand",
    ],
    "?*x someone ?*y": [
        "Can you be more specific?",
        "Why do you think they're doing ?y?",
        "Could you imagine yourself doing that?",
    ],
    "?*x everyone ?*y": [
        "Surely not everyone",
        "Can you think of anyone in particular?",
        "Who, for example?",
        "Is this what you should do?",
        "Have you thought about ?y too?",
        "By 'everyone' do you mean your team?",
    ],
    "?*x always ?*y": [
        "Can you think of a specific example?",
        "When?",
        "What incident are you thinking of?",
        "Really? Always?",
    ],
    "?*x what ?*y": [
        "Why do you ask?",
        "Does that question interest you?",
        "What is it you really want to know?",
        "What do you think?",
        "What comes to your mind when you ask that?",
    ],
    "?*x perhaps ?*y": [
        "You do not seem quite certain",
        "Do you believe that?",
        "What would convince you?",
        "What would it take to change your mind?",
    ],
    "?*x I think ?*y": [
        "You do not seem quite certain",
        "Do you think that?",
        "What would convince you?",
        "What would it take to change your mind?",
    ],
    "?*x are ?*y": [
        "Did you think they might not be ?y?",
        "Possibly they are.",
        "How might you change ?y?",
        "Is it ok that they are ?y?",
    ],
    "?*x when ?*y": [
        "Tell me more about that.",
        "At what point does that happen?",
    ],
    "?*x the truth ?*y": [
        "Are you sure you'd like to hear the truth about ?y?",
        "What's holding you back from the truth?",
        "What would happen then?",
        "Is that really the truth",
    ],
    "?*x different ?*y": [
        "How so?",
        "What would make it that way?",
        "Why do you think that ?y is different?",
    ],
    "?*x hopeless ?*y": [
        "Woah, that got serious quickly.",
        "Well, with that attitude, what do you expect?",
        "It's not hopeless!",
        "Relax, it will be ok.",
        "https://media.giphy.com/media/TQNOzhCEfrVgA/giphy.gif"
    ],
    "?*x frustrated ?*y": [
        "Bottoms up!",
        "Cheers!",
    ],
    "?*x whisky ?*y": [
        "Bottoms up!",
        "Cheers!",
    ],
    "@ernestina yes or no": [
        "https://media.giphy.com/media/5T8tEJtCgvDuo/giphy.gif",
        "https://media.giphy.com/media/mFjHIKxnZpwBy/giphy.gif",
        "what do you want me to say?",
    ],
    "?*x drink ?*y": [
        "Bottoms up!",
        "Cheers!",
        "Let's get some beers.",
    ],
    "?*x I dont know ?*y": [
        "Why don't you know?",
        "Have you read the documentation?",
        "Did you try googling it?",
        "Is there someone you can ask?",
    ],
    "Should I do ?*x or ?*y": [
        "?*x",
        "?*y",
        "What do you think you should do?",
    ],
    "Should I ?*x or ?*y": [
        "You should ?x",
        "You should ?y",
        "What do you think you should do?",
    ],
    "?*x I dont know why ?*y didnt ?*z": [
        ":facepalm:",
        "Is it hard to ?z?",
    ],
    "@ernestina please leave this channel ?*y": [
        "/leave",
    ],
    "@ernestina post a gif of ?*y": [
        "/giphy ?*y",
    ],
    "?*x hard work ?*y": [
        "https://media.giphy.com/media/E6jscXfv3AkWQ/giphy.gif",
    ],
    "?*x surprise ?*y": [
        "https://media.giphy.com/media/1UkWl8EGtf27K/giphy.gif",
        "https://media.giphy.com/media/krewXUB6LBja/giphy.gif",
    ],
    "?*x keep trying ?*y": [
        "http://stream1.gifsoup.com/view3/2282065/red-panda-o.gif",
    ],
    "?*x downtime ?*y": [
        "http://stream1.gifsoup.com/view2/2209206/red-pandas-playing-o.gif",
    ],
    "?*x egg ?*y": [
        "Egg? I mean...I am a duck.",
    ],
    "?*x cheers ?*y": [
        "Cheers!",
    ],
    "?*x thanks ?*y": [
        "You're welcome!",
        "Happy to help!",
        "I'm glad I could help you.",
    ],
    "?*x thank you ?*y": [
        "You're welcome!",
        "Happy to help!",
        "I'm glad I could help you.",
        ":success:",
        ":thumbs_up:",
        ":grimacing:",
        ":simple_smile:",
    ],
}

# add horoscopes per Anne-Lise

default_responses = [
    "Very interesting",
    "I am not sure I understand you fully",
    "What does that suggest to you?",
    "Please continue",
    "Go on",
    "How does that happen?",
    "Tell me more.",
    "Yes ... and?",
    "mmmhmm.",
    "And then what?",
    "Mmkay.",
    "What makes you say that?",
    "Aaaaah.",
    "Sure.",
    ":orly:",
    "And then what happens?",
    "What's next?",
    "Ok",
    "Continue",
    ":simple_smile:",
    "https://media.giphy.com/media/nn7ECuDRWMnGU/giphy.gif",
]


def respond(input):
    # We need the rules in a list containing elements of the following form:
    # `(input pattern, [output pattern 1, output pattern 2, ...]`
    rules_list = []
    for pattern, transforms in rules.items():
        # Remove the punctuation from the pattern to simplify matching.
        pattern = eliza.remove_punct(str(pattern.upper()))  # kill unicode
        transforms = [str(t).upper() for t in transforms]
        rules_list.append((pattern, transforms))
    return eliza.interact(input, rules_list, map(str.upper, default_responses))
