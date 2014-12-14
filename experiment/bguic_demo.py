import bguic

print("Selecting a new ui language")
bguic.select_language()

answer = bguic.yes_no_question("Make a wise choice")
print("\nAnswer to yes or no question: ", answer)

answer = bguic.text_input(font_size=16)
print("\nResponse to text_input query:", answer)

answer = bguic.yes_no_question("Font still big?")
print("\nFont still too big?: ", answer)

print("\nSetting global font")
bguic.set_global_font()

answer = bguic.text_input()
print("\nResponse to default text input query:", answer)

print("\nTesting class methods")
app = bguic.SimpleApp()
app.show_select_language()
print(app.show_text_input("Query from app"))
print(app.show_yes_no_question("Query from app"))

