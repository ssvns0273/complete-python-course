# ;LISTS AND TUPLE ........LISTS is a built in data type that store set of values . it can store element of different type (integer ,float , string,etc.) 
# syantax list 

marks = [33,34,45,46,67,42]
print(marks)
print(len(marks))
print(type(marks))

student = ["shivam",23,2,23,"varanasi"]
print(student)
print(student[0])
student[0] = ("shubham") # list value change
print(student) 

#LIST SLICING....similar to string slicing
#syntax..... listname [starting_idx : ending_idx] # ending idx is not included
marks = [33,34,45,46,67,42]
print(marks[1 : 4])
print(marks[: 4])
print(marks[1 : ])
print(len(marks))

#LIST METHOD.........
list = [2,1,3]
list.append(4) # add one element at the end[2,1,3,4] syntax-list.append(4)
print(list)
list.sort()     # sorts in ascending order [1,2,3,4] syntax-list.sort()
print(list)
list.reverse()  #reverse list [4,3,2,1] syntax-list.reverse() 
print(list)
list.sort( reverse=True )   #sorts in descending order syntax -list.sort( reverse=True )
print(list)
list = ["apple","banana","mango"]
list.sort( reverse=True )
print(list)

list = [1,2,3,4]
list.reverse()    #insert elemrnt at index # syntax-list.reverse() 
print(list)
list = [2,1,3,1]
list.remove(1)      #remove first occurrence of element[2,3,1] syntax-list.remove(1)
print(list)
list.pop(2)         #remove element at idx
print(list)