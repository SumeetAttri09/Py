#print("Hello World")

'''name = "Sumeet"
age = 20
print("my name is", name, "and I am ",age, "years old")'''

#print(type(age))

#total_price = 100

#sum of two numbers
# a=10
# b=20
# sum = a+b
# mul = a*b
# print(sum)
# print(a<b)
# print(a!=b)

# a-=55
# print(a)
# b+=5
# print(b)


# ans1 = int(5+10.0)
# ans2 = 5+10.0
# print(ans1, type(ans1))
# print(ans2, type(ans2))


# a = int(input("enter a number: "))
# b = int(input("enter another number "))
# sum = a+b
# print(sum)

# color = input("Enter color: ")

# if color == "red":
#     print ("stop")
# elif color == "yellow":
#     print("wait")
# else :
#     print("go")

# color = input("Enter color: ")
# match color:
#     case "red":
#         print ("stop")
#     case "yellow":
#         print ("wait")
#     case "green":
#         print ("go")
#     case "blue":
#         print ("ok")    
#     case _:
#         print("invalid")

#while loop
# cnt = 1
# while (cnt<=5):
#     print ("H W")
#     cnt+=1

#for loop
# string = "hello"
# for var in string:
#     print(var)    

#range
# for i in range(1,10):
#     print(i)


#string
# word = "python"
# print (len(word))

# word1 = ("I love")
# word2 = ("python")
# print (word1 + " " + word2)



#formatting
#1)normal formatting
# a=5
# b=10
# sum=a+b
# print("sum of a and b is: {}".format(sum))

#2)f-string formatting
#print(f"sum of {a} and {b} is {sum}")



#list
#marks = [10,20,40,50]
#print(len(marks))
#print(marks[1])
# marks.append(70)
# print(marks)



#tuple
tup = (10,20,30,40.5,"ab")
print(len(tup))
print(tup[0:2])
print(tup.index(20))
print(tup.count(20))



#Dicitionary
info = {
  "name": "aman",
  "class": "8th",
  "cgpa": "8.4"
}
print(info.keys())
#d.keys()
#d.values()
#d.items()
#d.get(val)
#d.update(new_item)




#sets(mutable): collection of unique elements(immutable)
s = {1,2,3,4,5}
print(type(s))
print(len(s))
print(s.add(6))
print(s.remove(5))
print(s)

empty_set = set()
print(type(empty_set))
#s.union(set2)
#s.intersection(set2)