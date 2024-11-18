# Import required libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('SimpleBot')

# Create and set up a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Function to chat with the bot
def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            bot_response = chatbot.get_response(user_input)
            print(f"Bot: {bot_response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Run the chatbot
chat_with_bot()
