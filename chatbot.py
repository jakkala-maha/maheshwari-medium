import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thank you!", "I'm doing well, thanks for asking."]),
    (r"what is your name?", ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]),
    (r"(.*) (weather|forecast) in (.*)", ["Fetching weather forecast for %3..."]),
    # Add more patterns and responses as needed
]

# Create a Chat instance
chatbot = Chat(patterns, reflections)

# Start the conversation loop
print("Welcome to the ChatBot. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("ChatBot: Bye! Have a great day.")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
