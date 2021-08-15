"""Global and Inter-function Variables"""

#Global variables can be used by everyone, both inside of functions and outside.
x = 15
def func1():
	print(x)
func1()	

#But here the function use the var value in the function giving it more priority, called Inter-function Variable.
#The variable 'y'(2nd one) in the following function is not a Global Variable(cannot be used by everone).
y = 25
def func2():
	y = 35
	print(y)
func2()

#Convert Inter-function Variable to Global Variable
def func3():
	global z
	z = 60
func3()	
print (z)


"""SPECIAL"""
a = "value"
def func4():
	global a
	a = "value overwrittened" #This variable has converted from Inter-Function to Global Variable
func4()
print(a) #Bacause of that the first value in 'a' variable overwritten to second value.
