# copndtional statement (syntax) 

"""if (condtion):
      statement1
 elif(condtion):
      statement2
 else:
     statementN """
# python is a INDENTATION LANGUAGE
# traffic signal
trafficlight = input("light:")
if(trafficlight == "red"):
    print("stop")
elif(trafficlight == "green"):
    print("go")
else:
    print("light is broken")
    # exampline 2 grade of student 
    marks =int(input("marks:"))
    if(marks >=90):
        print("A grade")
    elif(marks >= 80 and marks < 90):
        print("B grade")
    elif(marks >=70 and marks < 80):
        print("C grade")
    else:
        ("D grade")
