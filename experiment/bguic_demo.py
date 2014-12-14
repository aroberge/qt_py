import bguic

print("\n before asking yes or no question")
answer = bguic.yes_no_question("Make a wise choice")
print(answer)

print("Simple text input demo")
answer = bguic.text_input()
print(answer)

bguic.set_global_font()

print("Simple text input demo after changing global font")
answer = bguic.text_input()
print(answer)

print("choosing a new ui language")
bguic.choose_language()

print("Simple text input demo after changing language")
answer = bguic.text_input()
print(answer)

print("\n font setting after last locale change")
bguic.set_global_font()

