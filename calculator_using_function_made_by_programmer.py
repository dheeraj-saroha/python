a=input("Enter the first number :")
b=input("Enter the second number  :")
def sum () :
           c=a+b
           print("Sum of two number",c)
def sub () :
           c=a-b
           print("Difference of two number",c)
def mul () :
           c=a*b
           print("Product  of two number",c)
def div () :
           c=a/b
           print("Quotient of the number",c)
try : 
     a=int(a)
     b=int(b)
     choice=int(input("enter the choice : 1.sum\n 2.subtract\n 3.multiply\n 4.divide\n"))
     if choice==1 :
                    sum()
     elif choice==2 :
                    sub()
     elif choice==3 :
                    mul()
     elif choice==4 :
                    div()
     else :
            print("Enter the correct choice....")
except :
         print("Enter the number into numerical value.....")
