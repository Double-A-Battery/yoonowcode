import random

words = [' anger', ' animal', ' anniversary', ' announce', ' another', ' answer', ' apologize',' balance', ' balloon', ' ballot', ' barrier', ' battle', ' beauty',' cheat', ' cheer', ' chemicals', ' chemistry', ' chief', ' child', ' children']
hangman = ["o","o\n|","o\n|-"," o\n-|-","  o\n -|-\n /","  o\n -|-\n / \ "]
chosen = random.choice(words)
chosen = chosen.replace(" ","")
blank = []
for i in range(len(chosen)):
    blank.append("_")
Lives = 6
over = False
while over == False:
    change = False
    blankstring = ""
    for i in range(len(blank)):
        blankstring = blankstring + blank[i]+" "
    print(blankstring)
    letter = input("try and guess a letter: ")
    for i in range (len(chosen)):
        if letter == chosen[i]:
            blank[i] = letter
            change = True
    if change == False:
        print(hangman[6-Lives])
        Lives = Lives-1
    if Lives == 0:
        over = True
        WL = False
    complete = True
    for i in range(len(blank)):
        if blank[i] == "_":
            complete = False
    if complete == True:
        over = True
        WL = True

if WL == True:
    print("congratulations, you guessed the word correctly, the word was "+ chosen)

elif WL == False:
    print("you failed, try again, the word was " + chosen)