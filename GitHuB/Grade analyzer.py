# Author Jean Toussaint
# Class Py
# Date 3/22/2025


# Grade Analyzer


# input


print(" enter your name:")

ntest1 = input("enter test 1: ")
ntest2 = input("enter test 2: ")
ntest3 = input("enter test 3: ")
ntest4 = input("enter test 4: ")

      

if ntest1 < 0 or ntest2 < 0  or ntest3 < 0 or ntest4:
      print("Test scores must be greater than 0.")
      raise SystemExit

nlowergrade = input("Drop lowest? (Y/N): ").upper()


if nlowergrade =='y':
   if ntest1 < ntest2 and ntest1 < ntest3 and ntest1 < ntest4:
        faverage = (ntest1 + ntest2 + ntest3) / 3.0
   elif ntest2 < test1 and ntest2 < ntest3 and ntest2 < ntest4:
        faverage =(ntest2 + ntest3 + ntest4) / 3.0
   elif ntesr3 < ntest1 and ntest3 < ntest2 and ntest3 <  ntest4:
        faverage = (ntest3 + ntest4 + nest2) / 3.0
   elif ntest4 < ntest1 and ntest4 < ntest2 and ntest4 < ntest3:
         
      
                      


print(f"{sName}'s test average is {faverage}: 1f")                  



