#type casting 
#implicit type casting
a=15
b=5
a=a/b
print(a)

#implicit type casting
x=2.0
y=8
z=x+y
print(z)

x=float(2.150)
y=2
c=x+y
print (c)


#explicit type casting
name="ganesh"
age="21"
weight="69.5"
height="5.11"
gpa=9.5
print("name")
print(float(age))   
weight=float(weight)
print(weight)
gpa=int(gpa)
print(gpa)

#input function
name=input("what is ur name?")
age=int(input("what is ur age?"))
print(f"my name is {name} and my age is {age}")


#simple calculator
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=a*b
print(f"the product of {a} and {b} is {c}")

#absolute value 
x=-3
y=-6
z=7
result=abs(x)
result2=abs(y)
print(result)
print(result2)
result3=max(x,y,z)
print(result3)

import math 
print (math.pi)

g=10
resultg=math.sqrt(g)
print(resultg)

import math 
a=float(input("enter a number A : "))
b=float(input("enter a number B : "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"the hypotenuse of the triangle is {c}")


#if else 
age=int(input("enter your age: "))
if age>=18:
    print("you are eligible to vote")
else: 
        print("you are not eligible to vote")
if age==18:
    print("you are eligible to vote")
print (age)





#simple calculator 
x=int(input("enter first number: "))
y=int(input("enter second number: "))
operation=input("enter the operation you want to perform: ")
if operation=="+":
    result=x+y
    print(f"the sum of {x} and {y} is {result}")
elif operation=="-":
    result=x-y
    print(f"the difference of {x} and {y} is {result}")             
elif operation=="*":
    result=x*y
    print(f"the product of {x} and {y} is {result}")     
elif operation=="/":
    if y!=0:
        result=x/y
        print(f"the quotient of {x} and {y} is {result}")
    else:
        print("division by zero is not allowed")
else:    print("invalid operation")     