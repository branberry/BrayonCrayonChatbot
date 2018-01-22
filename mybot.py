from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from trainingData import getTrainingData

conversation = getTrainingData()
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

