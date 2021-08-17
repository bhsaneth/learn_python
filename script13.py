#Replace String
a="I am Saneth"
print(a.replace("a","m"))
print(a.replace(a[2],a[3]))

b=a.replace("a", "m")
print(b)


#Spilt String
#The split() method returns a list where the text between the specified separator becomes the list items.
c="Condrat, Marry"
print(c.split(",")) #Split using ','

d="Happy New Year"
print(d.split(" ")) #Split using "space"

e=d.split(" ")
print(e[0])
print(e[1])

f=e[2]
print(f)


#String Concatenation
var1=a.split(" ")
var2=var1[0]
var3=var1[1]
var4=var1[2]

var5=c.split(",")
var6=var5[0]
var7=var5[1].lower()

var8=d.split(" ")
var9=var8[0]
var10=(var8[1] + " "+var8[2]).lower()
print(" ")

print(var4+", "+var2+var7+" "+var6+" i"+var8[1][0].lower()+ " "+var10+".") #Using Lists and Array Values