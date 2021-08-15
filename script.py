#Creating Variable
var1 = "saneth" #Type is String
var2 = 120 #Type is Int
#OR
VAR1 = int(120)
vaR2 = str('Saneth')
#INT and STRING cannot join like following
var3 = var1+vaR2
print(var3)

print(VAR1)
print(vaR2)
#Variable names are case-sensitive

#You cannot add digits infront of Variable ex- "2abc". 
#It makes a Error
#AND
print(type(vaR2))
"""Above codes are Python Syntax"""
if 5>3:
	print("5 is bigger than 3")
		
if 3<7:
	print("Hello " +var1+ " !")

#Many Values to Multiple Variables
x,y,z = "1","2","3"
print(x)
print(y)
print(z)

#One Values to Multiple Variables
x1 = y1 = z1 = "orange"
print(x1)
print(y1)
print(z1)

#Unpack a Collection
grades = ["a","b","c"]
x2,y2,z2 = grades
print(x2)
print(y2)
print(z2)
