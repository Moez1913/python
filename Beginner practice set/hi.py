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

'''n1=int(input("Enter the Number"))
n2=int(input("Enter the Number"))
l1=list(range(1,n1+1)) 
l2=list(range(1,n2+1))
print(min(l1))'''

# Rverse a list:

'''num=[1,2,3,4,5,6]
rvs_num=num[::-1]
print(rvs_num)'''


# short a list :
'''li=[6,4,9,3,7,2,1]
li.sort()
print(li)'''

# chack a if a list contain a value:

'''num=[1,2,3,4,5]
v=3
if v in num:
    print("found")
else:
        print("not found")    '''
 
# count occurrances of an item in list

'''items=['apple','banana','apple','orange']
count=items.count('apple')
print(count)'''

#List comprehension:
#showing squar
'''num=[x**2 for x in range(5)]
print(num)'''

#Dictionary creation:
person={'name':'alic','age':25}
'''print(person)'''

# Accessing dictionary values:
'''print(person['name'])'''

# Adding a item a item to a dictionary:
person['city']='Rajshahi'
'''print(person)'''
# Remove an item from dictionary:
'''del person['age']
print(person)'''

#itareting over dictionary :
'''for key,value in person.items():
    print(key,value)'''
