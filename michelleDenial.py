import random

askMichelle = str(input("What do you want to know?\n")).lower()# first input
michelleAnswers = ["Nope, not happening", "It's not happening honey", "Look; I love my country, but I love my self more", "I said no", "No."]

if askMichelle.count("president") or askMichelle.count("please") >= 1:
    print(random.choice(michelleAnswers))
elif askMichelle.count("president") == 0:
    print("I'm not going to respond to that")

while True:
    askMichelle = str(input("What else do you want to know?\n")).lower()#every imput after that
    #michelleList = askMichelle.split() / what I was going to do originally
    michelleAnswers = ["Nope, not happening", "It's not happening honey", "Look; I love my country, but I love my self more", "I said no", "No."]

    if askMichelle.count("president") or askMichelle.count("please") >= 1:
        print(random.choice(michelleAnswers))
    elif askMichelle.count("bye") or askMichelle.count("goodbye") >= 1:
        print("Okay, Goodbye! Much love - Michelle Obama")
        break
    else: #askMichelle.count("president") == 0:
        print("I'm not going to respond to that")


#okay, using count, you don't have to search through the the list. Just look
#for the character with count(). If it's there, print, if it's not, don't print.
#putting everything inside while true reprompts the user!
#if you wanna break free, put it before the 0 count so the computer gets to it, before it goes over the list again
#don't forget .lower!!!
        
