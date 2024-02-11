import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.",]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!", "I'm just a computer program, so I don't have feelings, but thanks for asking.",]
    ],
    [
        r"quit",
        ["Goodbye, have a great day!"]
    ],
]

# Create a chatbot using the pairs
chatbot = Chat(pairs, reflections)

# Function to start the chat
def chat():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Start the chat
if __name__ == "__main__":
    chat()
