import bguic

print("Simple text input demo")
answer = bguic.text_input()
print(answer)

bguic.set_global_font()

print("Simple text input demo after changing global font")
answer = bguic.text_input()
print(answer)

