text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero").split()
new_text = []

for item in text:
    if ',' in item:
        new_text.append((item.replace(',', 'ing,')))
    elif '.' in item:
        new_text.append((item.replace('.', 'ing.')))
    else:
        new_text.append((item + 'ing'))
text = ' '.join(new_text)

print(text)
