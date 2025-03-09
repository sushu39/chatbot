import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"how are you?", ["I'm good. How about you?", "Doing well, what about you?"]],
    [r"what is your name?", ["I'm a chatbot created for CodeAlpha!", "You can call me CodeAlphaBot."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you soon!"]],
    [r"(.*)", ["I'm not sure how to respond to that. Can you rephrase?"]]
]


chatbot = Chat(pairs, reflections)


print("Hello! I'm a chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")