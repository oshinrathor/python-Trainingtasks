def chatbot():
    print("Hello! I am your chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()  # Take user input and convert it to lowercase for easier comparison
        
        # Check for greetings
        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! How can I assist you today?")
        
        # Check if the user asks a question
        elif '?' in user_input:
            print("Chatbot: That's an interesting question! I'll try my best to answer.")
        
        # Check for farewell or goodbye messages
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop and end the chat
        
        # Check for any other unrecognized input
        else:
            print("Chatbot: I'm not sure how to respond to that. Could you rephrase?")

# Run the chatbot
chatbot()
