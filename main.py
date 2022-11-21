from math import sqrt
a = input("How long is the first side? \n")
b = input("\nHow long is the second side? \n")

if a.isnumeric() != True or b.isnumeric() != True:
  quit("Invalid input, please restart program")
elif float(a) <= 0 or float(b) <= 0:
  quit("You cannot have a length be 0 or less")
  
c = sqrt((float(a)**2 + float(b)**2))
print("\nThe third side is " + str(c))