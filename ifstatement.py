# 1. Large and small value
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if a>b:
    print(a,"is larger than",b)
elif a<b:
     print(b,"is larger than",a)
# 2. Large and small value out of three
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if a>b:
    if a>c:
        Large = a 
    else:
        Large = c 
else:
    if b>c:
        Large = b 
    else:
        Large = c     
if a<b:
    if a<c:
        small = a 
    else:
        small = c 
else:
    if b<c:
        small = b 
    else:
        small = c

print("The large number is",Large,"and the smaller number is",small)                    
# 3. Number is odd or even
a=int(input("Enter the number"))
if a%2==0:
    print(a,"is a even number")
else:
    print(a,"is a odd number") 
# 4. Number is divisible by 10 or not
a=int(input("Enter the number"))
if a%10==0:
    print(a,"is a divisible by 10")
else:
    print(a,"is not divisible by 10")   
# 5. A parson is minor or major                    
age=int(input("Enter the age"))
if age>18:
    print("Person is major")
else:
    print("Person is minor")
# 6. Year is leap or not
year=int(input("Enter the year"))
if year%4==0:
    if year%100!=0:
        print(year,"is leap year")
else:
    print(year,"is not leap year")    
# 7. Validation of trinagle
a=int(input("Enter the first angle"))
b=int(input("Enter the second angle"))
c=int(input("Ennter the third angle"))
total_angle=a+b+c
if total_angle==180:
    print("Triangle is valid")
else:
    print("Triangle is invalid")    
# 8. Abosulate value
a=int(input("Enter the number"))
if a<0:
    print(a*(-1))
else:
    print(a)
# 9. Area of rectangle is greater than perimeter
l=5
b=6
area=(l*b)
perimeter=2*(l+b)
if(area>perimeter):
    print("Yes area is greater than perimeter ")
else:
    print("No area is greater than perimeter ")
# 10.Three points on straight line
x1,x2,x3=2,1,9
y1,y2,y3=10,5,6
a=x1*(y2-y1)+x2*(y3-y1)+x3*(y1-y2)
if(a==0):
    print("Points lies on stright line")
else:
    print("Points not lies on  stright line")
# 11. Point lies inside , outside or on circle
#Center of circle
x,y=2,5
#Radius of circle
radius=10
#Give coordinate
x1,y1=5,6
a=pow(x-x1,2)
b=pow(y-y1,2)
distance=pow(a+b,2)
if distance<radius:
    print("Point lies inside")
elif distance>radius:
    print("Point lies outside")
elif distance==radius:
    print("Point lies on circle")            
# 12. Numbers in words
a=int(input("Enter the number between 0 to 19"))
if a==0:
    print("Zero")
elif a==1:
    print("One") 
elif a==2:
    print("Two")    
elif a==3:
    print("Three")
elif a==4:
    print("Four")    
elif a==5:
    print("Five")    
elif a==6:
    print("Six")                               
elif a==7:
    print("Seven")    
elif a==8:
    print("Eight")    
elif a==9:
    print("Nine")    
elif a==10:
    print("Ten")    
elif a==11:
    print("Eleven")    
elif a==12:
    print("Twelven")    
elif a==13:
    print("Thirteen")    
elif a==14:
    print("Fourteen")    
elif a==15:
    print("Fifteen")    
elif a==16:
    print("Sixteen")    
elif a==17:
    print("Seventeen")
elif a==18:
    print ("Eighteen")
elif a==19:
    print("Nineteen")           
# 13. Give the grade
mark1=60
mark2=80
mark3=50
total=mark1+mark2+mark3
avg=total/3
if(avg<39 or mark1<39 or mark2<39 or mark3<39):
    print("Fail")
if(avg>40)and(avg<44):
    print("P")
if(avg>45)and(avg<49):
    print("C")
if(avg>50)and(avg<54):
    print("B")
if(avg>55)and(avg<59):
    print("B+")
if(avg>60)and(avg<69):
    print("A")
if(avg>70)and(avg<79):
    print("A+")
if(avg>80)and(avg<100):
    print("O")   