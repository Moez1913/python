# chake even or odd:
'''n=int(input("Enter your number:"))
if(n%2==0):
    print(f'{n} is even')
else:
    print(f'{n} is odd')    '''




# find the largest number:
'''a=int(input("Enter your first number:"))
b=int(input("Enter your 2nd number:"))
c=int(input("Enter your 3rd number:"))
d=int(input("Enter your 4rth number:"))
lrg=max(a,b,c,d)
print(lrg)
'''

#check prime number:
num=int(input("Enter your number: "))
if num>1:
    for i in range(2,int(num/2)+1):
        if(num%2==0):
            print(f'{num} is not a prime')
            break
    else:
        print(f'{num} is a prime')    
else:
    print(f'{num} is not a prime')

#Factorial of a number:

#Generate a list of Numbers 0 to N
# Sum of list elements:
#find the avarage of a list: