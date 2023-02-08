print("hello world") #output:hello world

x=10
y=20
print(x+y) #output:30

x=10
print(x) #output:10
print(type(x)) #output:<class 'int'>
x='abc'
print(x) #output:abc
print(type(x)) #output:<class 'str'>

numberList=[10,20,30]
print(numberList) #output:[10,20,30]
fruits=['apple','mango','kiwi']
print(fruits) #output:['apple', 'mango', 'kiwi']
marks=[80.5,90.0,60.8]
print(marks) #output:[80.5, 90.0, 60.8] 

numberSet={1,2,3,3,4,5}
print(numberSet) #output:{1,2,3,4,5}

numberTuple=(10,20,30)
print(numberTuple) #output:(10,20,30)

x=30
y=40
if x>y:
    print('x is greater than y')
else:
    print('y is greater than x') #output:y is greater than x

x=20
y=20
if x>y:
    print('x is greater than y')
elif x==y:
    print('x and y are equal') #output:x and y are equal
else:
    print('y is greater than x')


for i in range(1, 10):
    print(i, end=' ') #output:123456789

numberList=[10, 20, 30, 40, 50]
for i in numberList:
    print(i, end=' ') #output:1020304050

#Write a program that prints only even numbers from the given list of numbers.
for num in range(1,11):
    if num % 2 == 0:
     print(num, end=" , ") #output: 2 , 4 , 6 , 8 , 10

i=1
while i<=10:
    print(i, end=' ') #output: 1 2 3 4 5 6 7 8 9 10 
    i = i + 1

#Write a program to print factorial of a given number
num = 6
factorial = 1
if num < 0:
    print("Sorry, factorial doesn't present for negative number")
elif num == 0:
    print("The factorial of 0 is one")
else :
    for i in range(1, num + 1):
        factorial = factorial*i
        print("The factorial of",num, "is", factorial) #output:The factorial of 6 is 720

def print_hello_world():
    print("hello world")
print_hello_world()
