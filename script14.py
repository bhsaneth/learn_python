#String Format

"""
age=56 #Int
stat="My age is " #Str
statOut=stat+age
print(statOut) #This makes an Error
#Fact: (Str+Int) cannot be done
"""

#But
age2="56" #Str
stat2="My age is "
statOut2=stat2+age2
print(statOut2) #Works
#Fact: (Str+Str) canbe done

#So, fixing (Int+Str)
age3=56
stat3="My age is "
print(stat3 + format(age3)) #Using Format method

#SPECIAL
marks=67
saying="Mom, I have {} marks for the exam"
print(saying.format(marks))

children=5
era_of_saying=58
saying1="I wanna have {} children, when I am {} years old."
saying2="I wanna have {0} children, when I am {1} years old."
saying3="I wanna have {1} children, when I am {0} years old."
print(saying1.format(children,era_of_saying))
print(saying2.format(children,era_of_saying))
print(saying3.format(children,era_of_saying))

