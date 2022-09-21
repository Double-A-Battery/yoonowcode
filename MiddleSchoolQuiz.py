import random as rand# get random numbers

"""

Addition
Subtraction
Multiplication
Times tables
Division
Division with remainder

"""

def generate_question(lev=1,q_type=None):
  # question?
  if q_type == None:#type not specified
    question_type = rand.choice(["add","sub","mul","times","div"])# pick a random type
  else:
    question_type = q_type
  num1 = rand.randint(1,lev*10)
  num2 = rand.randint(1,lev*10)
  q_text="Invalid question type"
  if question_type=="add":
    answer=num1+num2
    q_text=rand.choice([f"{num1} people are in a room. {num2} people come in. How many are now there? ",f"There are {num1} fruits in a room. I add {num2} more. How many are there now? ",f"What is {num1} + {num2}? "])
  elif question_type=="sub":
    if num1<num2:
      num1,num2=num2,num1 # restrict result to positive numbers
    answer=num1-num2
    q_text=rand.choice([f"{num1} people walk into a room. {num2} people leave. How many are left? ",f"What is {num1} - {num2}? "])
  elif question_type=="mul":
    num1 = rand.randint(1,20)
    num2 = rand.randint(1,20)
    answer=num1*num2
    q_text=rand.choice([f"In a bus there are {num1} people going to work, {num2} times more people go home on that same bus. how many people are on the bus ride home? ",f"What is {num1} * {num2}? "])
  elif question_type=="times":#times tables: both numbers are from 1 to 12
    num1 = rand.randint(1,20)
    num2 = rand.randint(1,20)
    answer=num1*num2
    q_text=rand.choice([f"In a bus there are {num1} people going to work, {num2} times more people go home on that same bus. How many people are on the bus ride home? ",f"What is {num1} * {num2}? "])
  elif question_type=="div":# the answer is always a whole number
    num2 = rand.randint(1,12)
    answer = rand.randint(1,12)
    num1 = num2*answer
    q_text=rand.choice([f"{num1} fruits are shared between {num2} people. How many fruits does each person get? ",f"What is {num1} / {num2} ? "])
  return (q_text,answer)

def ask_question(quest):
  question,answer=quest
  rlans = None
  while rlans == None:
    try:
      rlans = int(input(question)) #user inputs
    except:
        print("enter a number")
  if rlans == answer:
    print("correct")
    for p in range(3):
      print("")
    return True
  else:
    print("wrong, the correct answer is:", answer)
    for p in range(3):
      print("")
    return False
def get_grade(score):
  if score**2>=10000:
    return "Perfect Score"
  if score>=90:
    return "A"
  if score>=80:
    return "B"
  if score>=60:
    return "C"
  return "F for fail"

num_questions=10
numcorrect=0
for i in range(num_questions):
  iscorrect = ask_question(generate_question())
  print("")
  if iscorrect:
   numcorrect+=1
total_score=numcorrect/num_questions*100
Grade = get_grade(total_score)
print("Number correct: "+str(numcorrect)+"/"+str(10))
print("Score: "+str(int(total_score))+"%")
print("your grade is: ", Grade)
