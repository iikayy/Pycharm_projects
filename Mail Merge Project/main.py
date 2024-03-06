with open("./input/Names/invited_names.txt") as f:
    names = f.readlines()

for name in names:
    with open("./input/letters/starting_letter.txt") as f:
        letter = f.read()
        content = letter.replace("[name]", name.strip())
    with open(f"./output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as f:
        new_letter = f.write(content)

