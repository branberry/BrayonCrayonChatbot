from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# training data
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I am doing great.",
    "You're Welcome",
    "Good morning!",
    "Good morning to you too!"
]

# generating chatbot
chatbot = ChatBot(
    "Brayon Crayon",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./database.sqlite3'
    )

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


print("Hello, my name is Brayon Crayon.")

while True:
    try:
        bot_input = chatbot.get_response(None)
    
    except (KeyboardInterrupt,EOFError, SystemExit):
        break

