
# Simple Python Chatbot

def chatbot():
    print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        
        elif "your name" in user_input:
            print("Chatbot: I am a simple chatbot created in Python.")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}")
        
        elif "date" in user_input:
            from datetime import date
            today = date.today().strftime("%B %d, %Y")
            print(f"Chatbot: Today's date is {today}")
        
        else:
            print("Chatbot: Sorry, I don't understand that. Can you rephrase?")

# Run chatbot
if __name__ == "__main__":
    chatbot()