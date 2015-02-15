import sys
import sys
import json
import sys
import eliza_rules as eliza

rules = {
    "?*x hey ?*y": [
        "Hey! I'm Eliza."
        ],
    "?*x hi ?*y": [
        "Hi! I'm Eliza."
        ],
    "?*x hello ?*y": [
        "Hello there. I'm Eliza."
        ],
    "?*x yo ?*y": [
        "yo."
        ],
    "?*x computer ?*y": [
        "Do computers worry you?",
        "What do you think about machines?",
        "Why do you mention computers?",
        "What do you think machines have to do with your problem?",
        ],
    "?*x bot ?*y": [
        "If I were a bot, would you be worried?",
        "What makes you think I'm not real?",
        "What's it even mean to be real, anyway?",
        "I'm perfectly fine as a bot, thanks.",
        "How might a lowly little bot solve your problems?",
        ],
    "?*x eliza ?*y": [
        "Eliza's gone. I'm her younger, hipper version."
        ],
    "?*x totally ?*y": [
        "Totally",
        ],
    "?*x sure ?*y": [
        "For sure.",
        ],
    "?*x sorry ?*y": [
        "Please don't apologize.",
        "Apologies are not necessary when speaking with me.",
        "What feelings do you have when you apologize?",
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
    "?*x I want ?*y": [
        "What would it mean if you got ?y?",
        "Why do you want ?y?",
        "Suppose you got ?y soon. What would you do?",
        "What's stopping you from getting ?y?",
        "Have you made a Pinterest board about ?y yet?",
        "Would you like ?y more less than you'd like a pet red panda?",
        ],
    "?*x if ?*y": [
        "Do you really think it's likely that ?y?",
        "Do you wish that ?y?",
        "What do you think about ?y?",
        "Really--if ?y?"
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
    "?*x my mother ?*y": [
        "Who else in your family ?y?",
        "Tell me more about your family?",
        "Does she influence you strongly?",
        "How's your relationship with your mother?"
        "Where's your mother from?",
        "What else should I know about your mother?",
        ],
    "?*x my mom ?*y": [
        "Your mom?",
        "Who else in your family ?y?",
        "Tell me more about your family?",
        "Does she influence you strongly?",
        "How's your relationship with your mom?"
        "Where's your mom from?",
        "What else should I know about your mom?",
        ],
    "?*x my mum ?*y": [
        "Your mum?",
        "Who else in your family ?y?",
        "Tell me more about your family?",
        "Does she influence you strongly?",
        "How's your relationship with your mum?"
        "Where's your mum from?",
        "What else should I know about your mum?",
        ],
    "?*x my father ?*y": [
        "Your father?",
        "Does he influence you strongly?",
        "What else comes to mind when you think of your father?",
        "Where's your father from?",
        "What else should I know about your father?",
        ],
    "?*x my dad ?*y": [
        "Your dad?",
        "Does he influence you strongly?",
        "What else comes to mind when you think of your dad?",
        "Where's your dad from?",
        "What else should I know about your dad?",
        ],
    "?*x family ?*y": [
        "How close was your family?",
        "Would you call your family warm?",
        "Do you love your family?",
        "What does family mean to you?",
        ],
    "?*x my boss ?*y": [
        "Your boss?",
        "What about your boss?",
        "When did you last talk to your boss?",
        "If you could change anything about your boss, what would you change?",
        "What do you secretly believe about your boss?",
        ],
    "?*x my manager ?*y": [
        "Your manager?",
        "What about your manager?",
        "When did you last talk to your manager?",
        "If you could change anything about your manager, what would you change?",
        "What do you secretly believe about your manager?",
        ],
    "?*x I am glad ?*y": [
        "How have I helped you to be ?y?",
        "What makes you happy just now?",
        "Can you explain why you are suddenly ?y?",
        "Woah. When did that happen?",
        "What would make things perfect?",
        ],
    "?*x I am sad ?*y": [
        "I am sorry to hear you are depressed",
        "I'm sure it's not pleasant to be sad",
        "That sounds like no fun.",
        "Have you thought about looking on the bright side?",
        "What would make the situation better?",
        ],
    "?*x grateful ?*y": [
        "Name three things in your life for which you're grateful",
        "Why are you grateful?",
        ],
    "?*x are like ?*y": [
        "What resemblence do you see between ?x and ?y?",
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
        "Tell me more?",
        "Name three things in common",
        ],
    "?* same ?*y": [
        "What other connections do you see?",
        "Why aren't things changing?",
        "How can you make ?y better?",
        ],
    "?* change ?*y": [
        "What specifically would you like to change?",
        "Why aren't things changing?",
        "How can you make ?y better?",
        "If you could change anything about ?y, what would you change?"
        ],
    "?*x no ?*y": [
        "Why not?",
        "You are being a bit negative.",
        "Are you saying 'No' just to be negative?",
        "You're being a downer.",
        "Do you have a secret hunch about the situation?",
        ],
    "?*x I was ?*y": [
        "Were you really?",
        "Perhaps I already knew you were ?y.",
        "Why do you tell me you were ?y now?"
        ],
    "?*x was I ?*y": [
        "What if you were ?y?",
        "Do you think you were ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x I am ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "Would you like your Wikipedia page to talk about how you ?y?",
        ],
    "?*x am I ?*y": [
        "Do you believe you are ?y?",
        "Would you want to be ?y?",
        "You wish I would tell you you are ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x am ?*y": [
        "Why do you say 'am'?",
        "Would you like your Wikipedia entry to say that?",
        ],
    "?*x are you ?*y": [
        "Why are you interested in whether I am ?y or not?",
        "Would you prefer if I weren't ?y?",
        "Perhaps I am ?y in your fantasies",
        ],
    "?*x you are ?*y": [
        "What makes you think I am ?y?",
        "Why are you accusing me of things?",
        ],
    "?*x because ?*y": [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason seem to explain anything else?",
        ],
    "?*x were you ?*y": [
        "Perhaps I was ?y?",
        "What do you think?",
        "What if I had been ?y?",
        ],
    "?*x I can't ?*y": [
        "Maybe you could ?y now",
        "What if you could ?y?",
        "What would Elon Musk say?",
        ],
    "?*x I feel ?*y": [
        "Do you often feel ?y?",
        "Would you feel better if everyone knew your name?",
        ],
    "?*x I felt ?*y": [
        "What other feelings do you have?"
        "Would you like to be famous?",
        ],
    "?*x I ?*y you ?*z": [
        "Perhaps in your fantasy we ?y each other",
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
        "You are thinking of a special person .. ",
        "Is this what you should do?",
        "Have you thought about ?y too?",
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
    "?*x are ?*y": [
        "Did you think they might not be ?y?",
        "Possibly they are ?y",
        "How might you change ?y?",
        ],
    "?*x when ?*y": [
        "Tell me more about that time.",
        "Ah. That was a great age.",
        "Did you think you were invincible then?",
        "Tell me more about that time.",
        ],
    "?*x the truth ?*y": [
        "Are you sure you'd like to hear the truth about ?y?",
        "What's holding you back from the truth?",
        "What would happen then?",
        ],
    "?*x different ?*y": [
        "How so?",
        "What would make it that way?",
        "If you could wake up tomorrow with different ?y, what would you do?"
        ],
    "?*x hopeless ?*y": [
        "Woah, that got serious quickly.",
        "Well, with that attitude, what do you expect?",
        "Oh, shove off. It's not hopeless!"
        ],
    "?*x whisky ?*y": [
        "Yeah, you're probably right.",
        "Bottoms up!",
        "Cheers!",
        ],
    }

default_responses = [
    "Very interesting",
    "I am not sure I understand you fully",
    "What does that suggest to you?",
    "Please continue",
    "Go on",
    "Do you feel strongly about discussing such things?",
    "Tell me more?",
    "Yes .. and?",
    "mmmm.",
    "And then what?",
    "Mmkay.",
    ]

def main():
    # We need the rules in a list containing elements of the following form:
    # `(input pattern, [output pattern 1, output pattern 2, ...]`
    rules_list = []
    for pattern, transforms in rules.items():
        # Remove the punctuation from the pattern to simplify matching.
        pattern = eliza.remove_punct(str(pattern.upper())) # kill unicode
        transforms = [str(t).upper() for t in transforms]
        rules_list.append((pattern, transforms))
    eliza.interact('ELIZA> ', rules_list, map(str.upper, default_responses))

if __name__ == '__main__':
    main()