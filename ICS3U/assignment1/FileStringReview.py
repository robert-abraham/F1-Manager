"""
Robert
ICS3UO
FileStringReview.py
May 14

Read Notes file, encrypt it using encryption rules, output to console and file.
"""

VOWELS = "aeiouAEIOU"

#Open Input File, read from it and save it to an array
with open(r"assignment1/NoteInput.txt", "r") as input_file:
    phrases = input_file.readlines()
input_file.close()

#Create and open new file, named "NoteOutput.txt"
output_file =  open("NoteOutput.txt", "w")

#Iterate through each sentence in phrase
for sentence in phrases:
    output_two = []

    #Convert to list and remove any leading and trailing whitespace.
    sentence = list(sentence.strip())
    
    #Print Initial Input and Output to file
    print("INPUT:",''.join((sentence)))
    output_file.write("INPUT:"+''.join((sentence))+"\n")

    #Iterate through each letter in sentence
    for index, letter in enumerate(sentence):
        
        #Check if Letter is not a vowel
        if letter not in VOWELS:
            #Append letter to list, and replace Letter with number the length of the list
            output_two.append(letter)
            sentence[index] = str(len(output_two))
            
    
    #Convert back from list to string and prints new sentence
    print(''.join((sentence)))
    output_file.write(''.join((sentence))+"\n")
    
    #Converts back from list to string, put it in uppercase form, and adds 
    #an additional seperator so that when the next sentence is outputing there is a space between them.
    print((''.join((output_two))).upper()+"\n")
    output_file.write((''.join((output_two))).upper()+"\n\n")

#Close Output File
output_file.close()