vowels = 'aeiouAEIOU'

with open(r"ICS3U\review1\Input.txt", "r") as file:
    phrases = file.readlines()
file.close()


for sentence in phrases:
    output_two = []
    sentence = list(sentence)
    for index, letter in enumerate(sentence):
        if letter in vowels:
            sentence[index] = '*'
            output_two.append(letter)
        if letter is " ":
            sentence[index] = "+"

    print((''.join((sentence)).upper()))
    print((''.join((output_two)).lower()))