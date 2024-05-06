#Get User Input
phrase = input("Please Input a Phrase for Analysis: ")

while True:
    num  = input("Please Input the Number to recieve every nth character in the sentence: ")
    try: 
        if int(num) < len(phrase) and num >0:
            break
    except:
        print("Must be integer and less than the number of characters of the original input and greater than 0.")

#String Method [start:end:step]
print(phrase[0::num])