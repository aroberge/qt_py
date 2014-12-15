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



####################################
name = bguic.text_input(message="What is your name?",
                        title="Mine is Reeborg.")
if not name:
    name = "Unknown person"


bguic.message_box(message="The following language selection will only affect"+
                  " the default GUI elements like the text on the buttons",
                  title="For information")
bguic.select_language()


bguic.message_box(message="If the text is too small or too large, you can fix that",
                  title="For information")
bguic.set_global_font()

bguic.message_box(message="Hello {}. Let's play a game".format(name),
                  title="Guessing game!")

guess = min_ = 1
max_ = 50
answer = randint(min_, max_)
title = "Guessing game"
while guess != answer:
    message = "Guess a number between {} and {}".format(min_, max_)
    prev_guess = guess
    guess = bguic.integer_input(message=message, title=title,
                          default_value=guess, min_=min_ ,max_=max_)
    if guess is None:
        quitting = bguic.yes_no_question("Do you want to quit?")
        guess = prev_guess
        if quitting:
            break
    elif guess < answer:
        title = "Too low"
        min_ = guess
    elif guess > answer:
        title = "Too high"
        max_ = guess
else:
    bguic.message_box(message="Congratulations {}! {} was the answer.".format(name, guess),
                      title="You win!")



