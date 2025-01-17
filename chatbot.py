responses = {"hello":"Hello! how are you?",
             "hi":"hi Whats up?",
             "how are you?":"I'm good, Thanks",
             "bye": "Goodbye"
             }

def get_responses(message):
    message = message.lower()
    answer=""
    if message in responses:
        answer=responses[message]
        # return responses[message]
    else:
        answer="I didn't understand"
    return answer
    

    
while True:
    user_input = input("you : ")
    answer = get_responses(user_input)
    print("Chatbot : ",answer)

