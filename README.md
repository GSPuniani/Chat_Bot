# Chat_Bot
Make School CS 1.0 Project

Project: CS 1.0 Help Bot

This project uses Python 3.7.4.

This chat bot asks users about whether they need more help in CS 1.0. If the user response is in the affirmative, then the chat bot provides a recommendation for seeking help for this course. If the user response is firmly negative, then the chat bot provides other recommendations, such as asking users to help others. If the user response is ambiguous, then the chat bot encourages the user to seek additional help.

The program primarily consists of a function called `get_bot_response(user_response)`, some print statements, and a while-loop. The while-loop prompts the user for a response to the question of whether the user would like more help, and the questions is repeated until the user types 'done'. The print statements provide instructions to the user. After the user enters a response, the `get_bot_response(user_response` function takes in the user response as a parameter and determines which category it falls under (positive, negative, or ambiguous) based on whether the response is in any of the pre-set lists of possible responses. The function returns a single item in the list using the `choice()` method in the `random` library, and the program prints this item as a response before re-prompting the user with the same question about help.
