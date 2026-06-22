
import datetime

print("🤖 AI Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello!")

    elif "time" in user:
        print("Bot:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        print("Bot:", datetime.datetime.now().strftime("%d-%m-%Y"))

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")