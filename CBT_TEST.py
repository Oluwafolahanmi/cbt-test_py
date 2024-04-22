print("you are to register for this exam first, then proceed to login with your registered details.")
name = [] 
stuid = []
scores = []
named = []
iden = []
v = 0
while v < 2:
    namee = input("enter your name: ")
    stud = input("enter your student ID: ")
    name.append(namee)
    stuid.append(stud)
    print("congratulations", namee, ". You have successfully registered for this test. Tests start as soon as registration is complete")
    v += 1
print("proceed to login to take test")
v = 0
b = int(input("how many students will take this test: "))
while v < b:
    print("\n\nlogin to take your test")
    nam  = input("Name: ")
    id = input("id: ")
    named.append(nam)
    iden.append(id)
    if nam in name:
        if id in stuid:
            print("welcome", nam)
            print("""Read the instructions carefully. This test contains five 
#       multiple-choice questions. Every correctly answered question 
#       adds 10 marks while wrong answers removes 5 marks from your score.
#       select your answers using the prefix for the option ie 1, 2, 3, 4 
#       Good luck""")
            que = ["How many infinity stones are there?", "What is the only food that cannot go bad?", "What is the most visited Tourist attraction in the world",
                   "Which is the heaviest organ in the human body?", "Who made the third most 3-pointers in the Playoffs in NBA history?" ]
            option = [["1. 3", "2. 5", "3. 6", "4. 10"], ["1. Dark chocolate", "2. Peanut butter", "3. Canned tuna", "4. Honey"], ["1. Eiffel Tower", "2. Statue of Liberty", "3. Great Wall of China", "4. Colosseum"],
                      ["1.  Brain", "2. Liver", "3. skin", "4. Heart"], ["1. Kevin Durant", "2. JJ Redick", "3. Lebron James", "4. Kyle Korver"]]
            ansd = ["3", "4", "1", "2", "3"]
            d = 0
            for i in que:
                index = que.index(i)
                print(index + 1, end=". ")
                print(que[index])
                for opt in option[index]:
                    print(opt)
                user_ans = input(": ")                
                if user_ans == ansd[index]:
                    d += 10
                else:
                    d -= 5
                    print("The correct answer is option", ansd[index])
            print("You have successfully completed your test")   
            print("you scored ", d, "out of 50")
            if d < 10:
                print("you have an F")
            elif d >= 10 and d < 20:
                print("you have a D")
            elif d >= 20 and d < 30:
                print("you have a C")
            elif d >= 30 and d < 40:
                print("you have a B")
            else:
                print("you have a Distinction")
            scores.append(d)
            v += 1
            # print("The next student can take their test now")
        else:
            print("invalid id")
            id = input("try again: ")
        
    else:
        print("student details not registered")
        break
    
k = scores.index(max(scores))
h = named[k]
f = iden[k]
l = max(scores)
print("the maximum score is ", l, "by ", h, "with registration number", f )


    


        
