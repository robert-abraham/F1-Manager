#Get User Input
phrase = input("Please Input a Phrase for Analysis: ")

#Creating a Translation Table, Where Multiple Unicode Charachters get removed from the orgional table, then using that translation table, I translate it with the .translate
print(phrase.translate(str.maketrans('', '', 'AEIOUaeiou')))