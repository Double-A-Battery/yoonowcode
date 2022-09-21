import random
score = 0
dicegrid = [[1,1,1,2],[1,1,2,1],[1,2,1,1],[2,1,1,1]]
for i in range (4):
   for j in range (4):
       dicegrid[i][j] = random.randint(1,6)
   print(dicegrid[i])
#Mesure rows
#check for even
if (dicegrid[0][0] % 2) == 0 and (dicegrid[0][1] % 2) == 0 and (dicegrid [0][2] % 2) == 0 and (dicegrid [0][3] % 2) == 0:
    print("first line is even, score +20")
    score = score + 20
if (dicegrid[1][0] % 2) == 0 and (dicegrid[1][1] % 2) == 0 and (dicegrid [1][2] % 2) == 0 and (dicegrid [1][3] % 2) == 0:
    print("second line is even, score +20")
    score = score + 20
if (dicegrid[2][0] % 2) == 0 and (dicegrid[2][1] % 2) == 0 and (dicegrid [2][2] % 2) == 0 and (dicegrid [2][3] % 2) == 0:
    print("third line is even, score +20")
    score = score + 20
if (dicegrid[3][0] % 2) == 0 and (dicegrid[3][1] % 2) == 0 and (dicegrid [3][2] % 2) == 0 and (dicegrid [3][3] % 2) == 0:
    print("fourth line is even, score +20")
    score = score + 20
#check for odd
if (dicegrid[0][0] % 2) != 0 and (dicegrid[0][1] % 2) != 0 and (dicegrid [0][2] % 2) != 0 and (dicegrid [0][3] % 2) != 0:
    print("first line is odd, score +20")
    score = score + 20
if (dicegrid[1][0] % 2) != 0 and (dicegrid[1][1] % 2) != 0 and (dicegrid [1][2] % 2) != 0 and (dicegrid [1][3] % 2) != 0:
    print("second line is odd, score +20")
    score = score + 20
if (dicegrid[2][0] % 2) != 0 and (dicegrid[2][1] % 2) != 0 and (dicegrid [2][2] % 2) != 0 and (dicegrid [2][3] % 2) != 0:
    print("third line is odd, score +20")
    score = score + 20
if (dicegrid[3][0] % 2) != 0 and (dicegrid[3][1] % 2) != 0 and (dicegrid [3][2] % 2) != 0 and (dicegrid [3][3] % 2) != 0:
    print("fourth line is odd, score +20")
    score = score + 20
#collums
#even
if (dicegrid[0][0] % 2) == 0 and (dicegrid[1][0] % 2) == 0 and (dicegrid[2][0] % 2) == 0 and (dicegrid[3][0] % 2) == 0:
        print("collum one even, score +20")
        score = score + 20
if (dicegrid[0][1] % 2) == 0 and (dicegrid[1][1] % 2) == 0 and (dicegrid[2][1] % 2) == 0 and (dicegrid[3][1] % 2) == 0:
        print("collum two even, score +20")
        score = score + 20
if (dicegrid[0][2] % 2) == 0 and (dicegrid[1][2] % 2) == 0 and (dicegrid[2][2] % 2) == 0 and (dicegrid[3][2] % 2) == 0:
        print("collum three even, score +20")
        score = score + 20
if (dicegrid[0][3] % 2) == 0 and (dicegrid[1][3] % 2) == 0 and (dicegrid[2][3] % 2) == 0 and (dicegrid[3][3] % 2) == 0:
        print("collum four even, score +20")
        score = score + 20
#odd
if (dicegrid[0][0] % 2) != 0 and (dicegrid[1][0] % 2) != 0 and (dicegrid[2][0] % 2) != 0 and (dicegrid[3][0] % 2) != 0:
        print("collum one odd, score +20")
        score = score + 20
if (dicegrid[0][1] % 2) != 0 and (dicegrid[1][1] % 2) != 0 and (dicegrid[2][1] % 2) != 0 and (dicegrid[3][1] % 2) != 0:
        print("collum two odd, score +20")
        score = score + 20
if (dicegrid[0][2] % 2) != 0 and (dicegrid[1][2] % 2) != 0 and (dicegrid[2][2] % 2) != 0 and (dicegrid[3][2] % 2) != 0:
        print("collum three odd, score +20")
        score = score + 20
if (dicegrid[0][3] % 2) != 0 and (dicegrid[1][3] % 2) != 0 and (dicegrid[2][3] % 2) != 0 and (dicegrid[3][3] % 2) != 0:
        print("collum four odd, score +20")
        score = score + 20
#corners
#even
if (dicegrid[0][0] % 2) == 0 and (dicegrid[3][0] % 2) == 0 and (dicegrid[3][3] % 2) == 0 and (dicegrid[0][3] % 2) == 0:
        print("corners all even, score +20")
        score = score + 20
#odd
if (dicegrid[0][0] % 2) != 0 and (dicegrid[3][0] % 2) != 0 and (dicegrid[3][3] % 2) != 0 and (dicegrid[0][3] % 2) != 0:
        print("corners all odd, score +20")
        score = score + 20
#Diagonals
#odd
if (dicegrid[0][0] % 2) != 0 and (dicegrid[1][1] % 2) != 0 and (dicegrid[2][2] % 2) != 0 and (dicegrid[3][3] % 2) != 0:
        print("Diagonal top left to bottom right odd, score +20")
        score = score + 20
if (dicegrid[0][3] % 2) != 0 and (dicegrid[1][2] % 2) != 0 and (dicegrid[2][1] % 2) != 0 and (dicegrid[3][0] % 2) != 0:
        print("Diagonal top right to bottom left odd, score +20")
        score = score + 20
#even
if (dicegrid[0][0] % 2) == 0 and (dicegrid[1][1] % 2) == 0 and (dicegrid[2][2] % 2) == 0 and (dicegrid[3][3] % 2) == 0:
        print("Diagonal top left to bottom right even, score +20")
        score = score + 20
if (dicegrid[0][3] % 2) == 0 and (dicegrid[1][2] % 2) == 0 and (dicegrid[2][1] % 2) == 0 and (dicegrid[3][0] % 2) == 0:
        print("Diagonal top right to bottom left even, score +20")
        score = score + 20
sum = 0
for i in range(4):
    for j in range(4):
        sum = sum + dicegrid[i][j]
print("total dice sum: ", sum,".", "plus", sum, "Points")
score = score + sum
print("you scored",score, "points")
