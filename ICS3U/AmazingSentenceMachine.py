#Get User Input
input = input("Please Input a Phrase for Analysis: ")


print("""
Original Phrase: {}
Upper Case: {}
Lower Case: {}
A's Replaced with E's: {}
Find 'Hello': {}
Word Count: {}
Sentence Count: {}
""".format(input, input.upper(), input.lower(), input.replace("a", "e"), input.find("Hello"), input.count(), input.count(".")))