a=int(input(" Entter the first number :"))
b=int(input(" Enter the second number :"))
ch=int(input(" Enter the choice : 1.sum\n 2.subtract\n 3.multiply\n)4.divide\n "))
if ch==1 :
            c=a+b
            print("The sum of number is =",c)
elif ch==2 :
           c=a-b
           print("The difference of number is =",c)
elif ch==3 :
           c=a*b
           print("The product  of number is =",c)
elif ch==4 :
           c=a/b
           print("The quotient of number is =",c)
else :
       print("Enter the correct choice...")
