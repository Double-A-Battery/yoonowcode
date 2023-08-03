import random
name = input("write a name here: ")
insults = [[name,"is the kind of guy that brings everyone so much joy when you leave the room."], [name, "wasn't born stupid he took lessons"], ["The people who tolerate", name, "on a daily basis are the real heroes."]]
print(insults[random.randint(0,2)])