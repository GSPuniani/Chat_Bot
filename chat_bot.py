# This bot asks if the user needs help with CS 1.0 

# choice() will randomly return an element in a list
from random import choice

# Input: a string called user_response, which is the user's input
# Output: a string, which is the bot's response to the user
# The function uses conditionals, lists, and choice() to provide an appropriate response to the user
def get_bot_response(user_response):

    # Add several potential user responses in each list, where each list is a category of user response
    # No capital letters are included in these lists because the .lower() method is used in the if-statements
    user_response_affirmative = [
        "yes",
        "definitely",
        "sure",
        "yeah",
        "yes, please"
        "ok",
        "yup",
        "couldn't hurt"
    ]
    user_response_negatory = [
        "no",
        "nope",
        "definitely not",
        "no thanks",
        "i'm good",
        "that's it"
    ]
    user_response_ambiguous = [
        "perhaps",
        "maybe",
        "possibly"
    ]

    #Add several bot responses in each list, where each list corresponds to a category of user response
    bot_response_affirmative = [
        "Attend office hours from 9-9:30am on Tuesdays and Thursdays in Jess' Zoom Room",
        "Try getting help from other students and TAs at CoWork on Tuesdays and Thursdays from 1:30-2:30pm",
        "Post questions on Piazza",
        "Set up study/coding times with other students",
        "Hit up any senior on Slack or Discord for help",
    ]
    bot_response_negatory = []
    bot_response_ambiguous = []

    # Check which category the user_response falls into and return a random bot response from the corresponding category
    # The .lower() method converts the string into lower-case so that the user can enter a response with capitalization
    if user_response.lower() in user_response_affirmative:
        return choice(bot_response_affirmative)
    elif user_response.lower() in user_response_negatory:
        return choice(bot_response_negatory)
    elif user_response.lower() in user_response_ambiguous:
        return choice(bot_response_ambiguous)
    else:
        return "Don't be afraid to take advantage of the support available to you!"


print("Welcome to CS 1.0 Help Bot!")
print("This chat bot will direct you to useful resources for CS 1.0.")
print("Simply follow the directions and type in a response when prompted.")
print("When you're ready to terminate the program, please enter 'done' when prompted for a response.")

while True:
    # Prompt user for a response
    user_response = input("Do you need more help with CS 1.0?")

    # Quits program when user responds with 'done'
    if user_response == "done":
        break

    # Call function for a response from the bot
    bot_response = get_bot_response(user_response)
    print(bot_response)



