import bguic

print("Simple text input demo")
answer = bguic.text_input()
print(answer)

bguic.set_global_font()

print("Simple text input demo after changing global font")
answer = bguic.text_input()
print(answer)

print("Simple text input demo with French locale")
answer = bguic.text_input(locale='fr')
print(answer)

print("\n font setting after last locale change")
bguic.set_global_font()