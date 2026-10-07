def chatbot():
    print("chatbot: hi! i am a simple chatbot.")
    print("chatbot:you can say ' hello', 'how are you', or 'bye'. ")
while True:
 user_input = input("you:").lower()
 if user_input == "hello": 
            print("chatbot: hi!")
 elif user_input == "how are you":
     print("chatbot: i'm fine, thanks!")
 elif user_input == "bye":
     print("chatbot:goodbye!")
     break
 else:
     print("chatbot: sorry, i don't understand that.")
     