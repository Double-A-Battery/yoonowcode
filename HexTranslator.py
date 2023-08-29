NumLetter = ["A","B","C","D","E","F"]
related = [10,11,12,13,14,15]
Phrase = input("Enter your number here: ")
choice = int(input("type 1 for TRANSLATE TO or type 2 for TRANSLATE FROM: "))
segment = []
translated =[]
hexvalues = []
calcressult = []
finalresult = 0
if choice == 2:
    for i in range(len(Phrase)):
        segment.append(Phrase[i])
    for i in range(len(Phrase)):
        hexvalues.append(1*16**(len(Phrase)-i-1))
    print(hexvalues)
    print(segment)
    for i in range(len(Phrase)):
        for j in range(6):
            if NumLetter[j-1] == segment[i-1]:
                translated.append(j+9)
    print(translated)
    for i in range(len(Phrase)):
        finalresult += translated[i-1]*hexvalues[i-1]
print(finalresult)
