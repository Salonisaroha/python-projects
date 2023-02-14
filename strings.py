# Strings are sequence of characters. It is datatype in python.
# Strings are always used in quotes.
"""name = "John"
print(type(name))
print(name[1]) # To excess letter o from name using index concepts. Indices always start from 0.
greeting = "Good Morning, "
print(greeting + name) # Here Two strings are concatenate.
print(greeting , name)

# name[3] = "d" cannot support means we cannot change strings.
# Strings slicing
print(name[0:3])

print(len(greeting)) # by using len we can find whole length of sentence.
# if you want to write an offer letter.
letter = '''Dear <|NAME|>
You are selected!
<|DATE>'''
name = input ("enter your name")
date = input("enter date")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE>",date)
print(letter)
# To find doublespace in string.
mylines = "hello peers we are learning python nowadays Here we are discussing about    strings properties"
doublespace = mylines.find("  ")
print(doublespace)
# Escape sequences
# 1. \n
# 2. \t
letter1 = "Hello, viewers.\nI hope all are doing well\nI am happy to tell you that you are selected in our team noreply\n Email is salo@12234@gmail.com\n"
print(letter1)

# List and tuples
# Pyhton list are container to store a set of values of any datatype.It is in ordered way.
value = [1,2,3,4,5,6,7,8,9]
print(value)
#Properties :- List can be changed.
# We can create a list of items with different datatypes.
print(value[0])
value[3] = 9
print(value)
mynum1 = ["harry", 3,4,False,"saloni"]
print(mynum1)
print(mynum1[0:4]) # Slicing

mynum12 = [5,6,9,2,5,8]
mynum12.sort() # arrange list according to ascending order.
mynum12.reverse() # arrange list to reverse order
mynum12.append(7) # to add values to the end of the list.
mynum12.insert(6,7) # to add values to the list according to the index number.
mynum12.pop(6) # TO remove any value from the list according to the index.
mynum12.remove(8) 
print(mynum12)

# Tuples
# Tuples cannot be updated. It is immutable.
values_in_tuples = (23,56,87,65,90)
tuple1 = (1,)
print(values_in_tuples)

# Write a program to store  fruits in a list entered by the user.

fruits = [input("Enter fruits name of youe chice")]
print(fruits)
marks = [87, 98, 86, 79]
marks.sort()
print(marks)
print(marks[0] + marks[1] + marks[2] + marks[3])

# OR

print(sum(marks))

# write a program to count the number of zeros in the following tuple
# a = (5,0,7,0,9)

a = (5,0,7,0,9)
print(a.count(0))
 # Dictionary 
# It is collection of key values pair.
mydic = {
    "quality":"This is very precious gift for us.",
    "quantity":"it depends on the user how will he or she predict it.",
    "marks":[98,99,100,87],
    "anotherdict":{'saloni':'she is girl.'}
}
print(mydic["quality"])
print(mydic["anotherdict"]["saloni"]) # Nested dictionary.
mydic["marks"] = [87,67]
print(mydic["marks"])
# Properties of python dictionary.
1. It is unordered.
2.It is mutable.
3. It is Indiced.
4. 
print(mydic.keys()) # Here it is dict_keys. It gives all the keys of dictionary.
print(list(mydic.keys())) # Here it is converted into list.
print(mydic.values()) # It give all the values of dictionary.
print(mydic.items()) # It gives all the content of dictionary.
updated = {
    "friends":"Aman Dhttarwal",
    "role Model":"Shradha khapra"
}
mydic.update(updated) # updates the dictionary by using any value pair and updated keyword.
print(mydic)
print(mydic.get("quality1")) # Here get is used because it will no throw an error even saloni1 is not present in the class but given method will throw an error. Here get return none.
print(mydic["quality"])"""

# Sets 
# Sets is a collection of non repetitive elements.An empty syntax can be created by using below syntax.
y = set()
print(type(y))
y.add(4)
y.add(8)
print(y)

x = {1,2,3,4,5,4,5} # sets does not take repitative values.
print(x)
# Properties of set
# 1. sets are unordered.
# 2. Sets are unindex.
# 3. there is no way to change values in sets.

x.remove(2) # it remove elements from x.
print(x)
print(len(x)) # it provide length of x
x.pop # removes an arbitrary elements from the sets and returns the element removes.
print(x)
 # Practice set
mydict = {
 "pankha":"fan",
 "dabba":"fan",
 "Vastu":"things"
 }
print("options are", mydict.keys())
a = input("Enter the Hindi word : ")
print("The meaning of your word is", mydict.get(a))
 
num1 = int(input("enter number 1\n"))
num2= int(input("enter number 2\n"))
num3 = int(input("enter number 3\n"))
num4 = int(input("enter number 4\n"))
num5 = int(input("enter number 5\n"))
num6 = int(input("enter number 6\n"))
num7 = int(input("enter number 7\n"))
num8 = int(input("enter number 8\n"))
set = {num1,num2,num3,num4,num5,num6,num7,num8}
print(set)


