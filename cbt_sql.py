import mysql.connector as connection
import random
import time
mydb = connection.connect(host="127.0.0.1", user = "root", password = "Ademola.1234", database = "mydatabase")
mycursor = mydb.cursor()
# mycursor.execute("CREATE  TABLE students (Sn INT PRIMARY KEY AUTO_INCREMENT, fname CHAR(55), lname CHAR(30), Matric_no INT, Test_score INT, Admission_status CHAR(20), password VARCHAR(20), attempt INT, gender CHAR(10), State_of_origin CHAR(100), Address VARCHAR(200), Course CHAR(200))")
# mycursor.execute("DROP TABLE students")
def reg():
    print("\nRegister for this program")
    Fname = input("First name: ")
    lname = input("last name: ")
    matricNo = random.randint(200000, 300000)
    password = input("password:  ")
    conpassword = input("Confirm password: ")
    while password != conpassword:
        print("Password does not match")
        password = input("Enter your password: ")
        conpassword = input("Confirm your password: ")
    gender = input("Gender: ")
    Address = input("Address: ")
    Course = input("Course of study: ")
    State = input("State of Origin: ")
    adstat = "not yet admitted"
    print("congratulations", Fname, lname, "You have successfully registered for this program. Your matric number is", matricNo)
    querry = "INSERT INTO students (Fname, lname, Matric_no, Test_score, Admission_status, password, attempt, gender, State_of_origin, Address, Course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    deta = (Fname, lname, matricNo, 0, adstat, password, 0, gender, State, Address, Course)
    mycursor.execute(querry, deta)
    mydb.commit()
    put = input("Do you want to register another student? yes or no: ")
    if put == "yes":
        reg()
    elif put == "no":
        login()
def relist():
    sql = "SELECT * FROM students"
    mycursor.execute(sql)
    details = mycursor.fetchall()
    # print(details)
    relist = list(zip(*details))
    return relist
def login():
    print("\nLOGIN")
    print("\nwelcome to login")
    global mat
    mat  = int(input("Matric no: "))
    password = input("password: ")
    detail = relist()
    if mat in detail[3]:
        k = detail[3].index(mat)
        # print(k)
        if password == detail[6][k]:
            print("welcome", detail[1][k], detail[2][k])
            homepage()
        else:
            print("invalid id. try again")
            login()
    else:
        print("student details not registered. try again")
        start()
def start():
    decision = input("1. Register          2. Login         3. Quit")
    if decision == "1":
        reg()
    elif decision == "2":
        login()
def homepage():
    decision = input("1. CBT         2. Check result       3. Check Admission status         4. Logout")
    if decision == "1":
        test()
    elif decision == "2":
        checkResult()
    elif decision == "3":
        checkStatus()
    else:
        start()
def test(): 
    count = 0
    detail = relist()
    if mat in detail[3]:
        k = detail[3].index(mat)
        if detail[7][k] == 0:  
            print("""Carefully read the instructions. This test contains 5 questions. For every correct answer, you get 20 marks and every wrong answer removes 5 marks from your
                 score. Score of 70 and above gets you admitted. Goodluck. """)  
            que = ["\nHow many infinity stones are there?", "What is the only food that cannot go bad?", "What is the most visited Tourist attraction in the world",
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
                    d += 20
                else:
                    d -= 5
                    print("The correct answer is option", ansd[index])
            # time.sleep(5) 
            count += 1 
            stat = "UPDATE students SET attempt = %s WHERE Matric_no = %s"
            stat1 = (count, mat)
            mycursor.execute(stat, stat1)
            mydb.commit()      
            print("You have successfully completed your test") 
            if d > 70:
                stat = "UPDATE students SET Admission_status = %s WHERE Matric_no = %s"
                statget = "ADMITTED"
                stat1 = (statget, mat)
                mycursor.execute(stat, stat1)
                mydb.commit()
            else:
                stat = "UPDATE students SET Admission_status = %s WHERE Matric_no = %s"
                statget = "NOT ADMITTED"
                stat1 = (statget, mat)
                mycursor.execute(stat, stat1)
                mydb.commit()        
            sql = "UPDATE students SET Test_score = %s WHERE Matric_no = %s"
            get = (d, mat)
            mycursor.execute(sql, get)
            mydb.commit()
            # Test_score = d
            # time.sleep(5) 
            homepage() 
        else:
            print("You have already taken this test.")
            # time.sleep(5)
            decision = input("1. Check Result      2. Check Admission status     3. Logout")
            if decision == "1":
                checkResult()
            elif decision == "2":
                checkStatus()
            else:
                start()
def checkResult():
    detail = relist()
    if mat in detail[3]:
        k = detail[3].index(mat)
        if detail[7][k] == 1: 
            print("processing...")
            time.sleep(2)
            print(f"First Name: {detail[1][k]}  \nLast Name: {detail[2][k]}  \nTest score: {detail[4][k]}   \nMark Obtainable: 100   \nPercentage score: {detail[4][k]}%")
            # time.sleep(5)
            des = input("\n1. Homepage     2. Admission status     3. Logout")
            if des == "1":
                homepage()
            elif des == "2":
                checkStatus()
            else:
                start()
        else:
            print("processing...")
            time.sleep(2)
            print("You do not have a result yet as you have not taken the test")
            des = input("1\n. Homepage     2. Take test     3. Logout")
            if des == "1":
                homepage()
            elif des == "2":
                test()
            else:
                start()
def checkStatus():
    detail = relist()
    if mat in detail[3]:
        k = detail[3].index(mat)
        if detail[7][k] == 1:
            if detail[5][k] == "ADMITTED":  
                print("processing...")
                time.sleep(2)
                print("ADMISSION DETAILS")
                print(f"First Name: {detail[1][k]}  \nLast Name: {detail[2][k]} \nAddress: {detail[10][k]} \nState of Origin: {detail[9][k]}  \nStatus: {detail[5][k]} \nCourse of study: {detail[11][k]}  \nMatric No: {detail[3][k]}  \nDuration of Study: Four years    \n\nUniversity of Folahanmi \nBobo Chicago.\nVice Chancelor")
                # time.sleep(5)
                des = input("\n1. Homepage     2. Check Result     3. Logout")
                if des == "1":
                    homepage()
                elif des == "2":
                    checkResult()
                else:
                    start()
            elif detail[5][k] == "NOT ADMITTED":
                print("processing...")
                time.sleep(2)
                print("ADMISSION DETAILS")
                print(f"First Name: {detail[1][k]}  \nLast Name: {detail[2][k]} \nAddress: {detail[10][k]} \nState of Origin: {detail[9][k]}  \nStatus: {detail[5][k]} \n")
                # time.sleep(5)
                des = input("\n1. Homepage     2. Check Result     3. Logout")
                if des == "1":
                    homepage()
                elif des == "2":
                    checkResult()
                else:
                    start()  
        else:
            print("no amission status yet. proceed to take the test.")
            homepage()             
start()
