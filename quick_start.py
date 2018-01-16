from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ron Obvious")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing fuck.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
"""
count = 0
while count < 100:
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)
    count += 1
"""
response = chatbot.get_response("How do you do")
print(response)
