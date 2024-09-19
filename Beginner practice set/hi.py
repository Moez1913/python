#add,subtrac,multiply,division,exponant,Modulus two number 
'''a=20
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)'''

#simple interest calculation:
'''
principal=1000
rate=5
time=2
interest=(principal*rate*time)/100
print(interest)
'''
# are of circle
'''
import math
redius=5
area=math.pi*(redius*2)
print(area)
'''

#convert celcius to fahrenheit
'''
cl=25
fh=(cl*(9/5))+32
print(fh)
'''

# chake even or odd
'''
n=int(input("enter your number"))
if n%2==0:
    print("even")
else:
    #print("odd")
    '''

# find the largest number 
"""
a=int(input("Enter the first number:"))   
b=int(input("Enter the 2nd number:"))   
c=int(input("Enter the 3rd number:"))   
largest=max(a,b,c)
print(largest)"""

#check prime number

'''num=int(input("Enter your Number:"))
if num>1:
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            print(f'{num} is not prime')
            break
    else:
        print(f'{num} is prime')    
else:
    print(f'{num} is not prime')'''
         
#Factorial of a number:
'''import math

num=int(input("Enter your Number:"))
fac=math.factorial(num)
print(fac)'''

#Generate a list of Numbers 0 to N

'''n=int(input("Enter the Number"))
numbers=list(range(1,n+1))
print(numbers)'''

# Sum of list elements:
'''n=int(input("Enter the Number"))
numbers=list(range(0,n+1))
total=sum(numbers)
print(total)'''

#find the avarage of a list:
'''n=int(input("Enter the Number"))
numbers=list(range(1,n+1))
avrg= sum(numbers)/len(numbers)
print(avrg)'''

#find minimum and maximum in a list;

n1=int(input("Enter the Number"))
n2=int(input("Enter the Number"))
l1=list(range(1,n1+1))
l2=list(range(1,n2+1))
print(min(l1))


