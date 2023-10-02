#if else
a=25
if a>30:
    print("Yes a is greater then 30")
elif a>20:
    print("Yes a is greater then 20")
else:
    print("Yes a is greater then 10")

#input
a=input("Enter Your Name ")
b=int(input("Enter Your Age "))
print("Your name is",a,"age is",b)

#loop
#while Loop
a=1
while(a<11):
    print(2*a)
    a+=1
else:
    print('completed')


b=1
while(a<3):
    print(2*a)
    a+=1
    if b==3:
        break
else:                           #here else statement will not run
    print('completed')

#for loop
a='abcd'
for i in a:
    print(i)

l=[1,2,8,'hh',5+5j,54.5]
for i in l:
    print(type(i))
    if i==2:
        continue
else:
    print("this will be executed once loop will complete itself succesfully")    
