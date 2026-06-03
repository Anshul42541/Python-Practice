letter = """Dear <|NAME|>, 
You are selected.
<|DATE|>"""

print(letter.replace("<|NAME|>", "Anshul").replace("<|DATE|>", "27 MAY 2026"))