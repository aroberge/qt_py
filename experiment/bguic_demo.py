import bguic
from random import randint

#print("Selecting a new ui language")
#bguic.select_language()
#
#answer = bguic.yes_no_question("Make a wise choice")
#print("\nAnswer to yes or no question: ", answer)
#
#answer = bguic.text_input(font_size=16)
#print("\nResponse to text_input query:", answer)
#
#print("Selecting a new ui language")
#bguic.select_language()
#
#answer = bguic.yes_no_question("Font too big?")
#print("\nFont too big?: ", answer)
#
#if answer:
#    print("\nSetting global font")
#    bguic.set_global_font()
#
#answer = bguic.text_input()
#print("\nResponse to default text input query:", answer)
#
#print("\nTesting class methods")
#app = bguic.SimpleApp()
#app.show_select_language()
#print(app.show_text_input("Query from app"))
#print(app.show_yes_no_question("Query from app"))


####################################
bguic.message_box(message="Let's play a game", title="Guessing game!")
min_ = 1
max_ = 50
answer = randint(min_, max_)
print(answer)
guess = 0
title = "Guessing game"
while guess != answer:
    message = "Guess a number between {} and {}".format(min_, max_)
    guess = bguic.integer_input(message=message, title=title,
                          default_value=guess, min_=min_ ,max_=max_)
    if guess < answer:
        title = "Too low"
        min_ = guess
    elif guess > answer:
        title = "Too high"
        max_ = guess

bguic.message_box(message="{} was the answer".format(guess), title="You win!")



