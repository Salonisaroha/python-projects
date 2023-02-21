"""marks = 0
while(marks<50):
    print(marks)
    marks += 1
fruits = ["Mango", "kiwi", "apples", "watremelon"]
i = 0
while(i<len(fruits)):
    print(i)
    i = i + 1
 # For loop :- A for loop is used to iterate through a sequence like list, tuple or string.
veges = ["brinjal","potatoes","cauliflower","capsicum"]

for i in veges:
    print(i)
 # Range function in pyhton is used to generate a sequence of characters.
for i in range(0,7):
    print(i)
# For loop with else
for item in range(10):
    if item == 5:
        break 
    print(item)
else:
    print("this is exhausted")# This is run when whole loop is successfully terminated.

for num in range(8):
    if num == 5:
        continue
    print(num)
else:
    print("this is exhausted")

 # Pass statement is a null statement in python. It instructs "do nothing".
value = [1,4,6,8]
for x in value:
    pass # If we want to add another code later, but enable to pass the next code because it will show an error. To avoid this error we use pass statement which means do nothing.

print("pass is a a null statement")
i = 2
for item in range(1,11):
    print(item*i)
    #Or
num = 2
value = 0
while(num<21 and value<=10):
    
    print(num*value)
    value = value + 1
num = int(input("enter any number"))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("this is prime")
else:
    prime("this is not prime number.")
num = int(input("enter any number"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * 1
print(f"The factorial of {num} is {factorial}")

for i in range(4):
    print("*"*(i +1))"""
n = 3
for item in range(3):
    print(" " * (n-item-1), end = "")
    print(" " * (2*item +1), end = "")
    print(" " * (n-item-1))
x = 3
for i in range(3):
    print(" " * (i*3))
    print(" " * (x-i), end = "")
    print(" " *(i*x) )










