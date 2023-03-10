# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as individual_letter:
            individual_letter.write(new_letter)
