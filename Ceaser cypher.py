Number = (0)
Placehold =("")
Placenumber = (0)
Valid = False
Revamp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphacaps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
RevampCaps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(alphabet)):
    alphacaps[i] = alphabet[i].upper()
while Valid == False:
    try:
        Number = int(input("How many places is the cypher being moved? "))
    except:
        print("enter an integer value")
    else:
        Valid = True
for i in range(26):
    Placehold = alphabet[i-1]
    Placenumber = i - 1 + Number
    if Placenumber > 25:
        Placenumber -= 26
    if Placenumber < 0:
        Placenumber += 26

    Revamp[Placenumber] = Placehold
for i in range(len(Revamp)):
    RevampCaps[i] = Revamp[i].upper()


message = input("enter the message you cant to encrypt or decrypt: ")
FM = ""

for i in range (len(message)):
    Placehold = message[i]
    try:
        Placehold = int(Placehold)
    except:
        if Placehold == " ":
            FM =+ " "
        else:
            for j in range (len(alphabet)):
                if Placehold == alphabet[j]:
                    FM += Revamp[j]
                if Placehold == alphacaps[j]:
                    FM += RevampCaps[j]
    else:
        FM += str(Placehold)
print(FM)
