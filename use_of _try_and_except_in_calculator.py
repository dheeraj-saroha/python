a=input("Enter the first number :")
b=input(" Enter the second number :")
try :
      a=int(a)
      b=int(b)
      choice=int(input(' Enter the choice : 1.sum\n 2.subtract\n 3.multiply\n 4.divide\n '))
      if choice ==1 :
                      c=a+b
                      print(" sum of number is =",c)
      elif choice ==2 :
                      c=a-b
                      print(" difference of number is =",c)
      elif choice ==3 :
                      c=a*b
                      print(" product of number is =",c)
      elif choice ==4 :
                      c=a/b
                      print(" quotient of number is =",c)
      else : 
             print("Enter the correct choice .....")
except :
         print("Enter the numerical value...")
        
