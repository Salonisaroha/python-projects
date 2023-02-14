
print("hello world")

# here commas are used to write strings in different lines instead of comments.
 
print(''' Twinkle twinkle little star,
how  i  wonder what you are
up above the world so high
like a diamond in the sky''') 

# given below names are all strings.

name = '''saloni''' 
name1 = "saloni"
name2 = 'saloni'

# checking type

print(type(name))
print(type(name1))
print(type(name2))

# typecasting  or typeconversions

a = 678
b = 89.98
print(float(a))
print(int(b))
print(a + b)

# To make calculator using python programming

firstnum = input("enter any num1 ")
operator = input("enter operator [+,-,*,/,%]" )
secondnum = input("enter any num2 ")
firstnum = int(firstnum)
secondnum = int(secondnum)
if operator == "+" :
     print("sum of firstnum and secondnum is : ", firstnum + secondnum)
if operator == "-" :
     print("differnce of firstnum and secondnum is : ", firstnum - secondnum)
if operator == "*" :
     print("multiplication of firstnum and secondnum is : ", firstnum * secondnum)
if operator == "/" :
     print("division  of firstnum and secondnum is : ", firstnum / secondnum)
if operator == "%" :
     print("remainder of firstnum and secondnum is : ", firstnum % secondnum)

# To find sum of two numbers
#   
num1 = input("enter no. 1 : ")
num2 = input("enter second num2 : ")
num1  = int(num1)
num2 = int(num2)
print("sum of two numbers is : ", num1 + num2)

# To find remainder of number

mynum1 = input("enter number : ")
mynum1 = int(mynum1) 
print("remainder of this number is : ", mynum1%2)

# Input is always comes in string you have to convert according to your convience.
a = 45
b = 60
print(a>b)   # comparision operators are always comes in booleans.
digit1 = input("enter ist no. : ")
digit2 = input("enter 2nd no. : ")
digit1 = int(digit1)
digit2 = int(digit2)
print("average of two numbers is : ",(digit1 + digit2)/2)

# To calculate square of number

a = input("enter no. :")
a = int(a)
print("square of no. is : ", a*a)