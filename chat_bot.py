# This bot asks if the user needs help with CS 1.0 

# choice() will randomly return an element in a list
from random import choice

# Input: a string called user_response, which is the user's input
# Output: a string, which is the bot's response to the user
# The function uses conditionals, lists, and choice() to provide an appropriate response to the user
def get_bot_response(user_response):

    # Add several potential user responses in each list, where each list is a category of user response
    user_response_affirmative = []
    user_response_negatory = []
    user_response_ambiguous = []

    #Add several bot responses in each list, where each list corresponds to a category of user response
    bot_response_affirmative = []
    bot_response_negatory = []
    bot_response_ambiguous = []

    # Check which category the user_response falls into and return a random bot response from the corresponding category
    if user_response in user_response_affirmative:
        return choice(bot_response_affirmative)
    elif user_response in user_response_negatory:
        return choice(bot_response_negatory)
    elif user_response in user_response_ambiguous:
        return choice(bot_response_ambiguous)
    else:
        return "Don't be afraid to take advantage of the support available to you!"


print("Welcome to CS 1.0 Help Bot!")
print("This chat bot will direct you to useful resources for CS 1.0.")
print("Simply follow the directions and type in a response when prompted.")
print("When you're ready to terminate the program, please enter 'done' when prompted for a response.")

while True:
  user_response = input("Do you need help with CS 1.0?")
  
  # Quits program when user responds with 'done'
  if user_response == "done":
    break

  
  bot_response = get_bot_response(user_response)
  print(bot_response)



