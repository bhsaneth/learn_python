#Check String (True or False)

#Using 'in' keyword
txt="Hi, I love you so much"
print("love" in txt)
print("Love" in txt)

txt2="True or False"
print("True" in txt2)
var1="True" in txt2
print(var1)

txt3="Check me"
print("check" in txt3)
var2="me" in txt3

#Using 'if' statement
txt4="I want to read you"
if "eat" in txt4:
	print("'read' word is available.")
else:
	print("'read' word is unavailable.")

txt5="Son or Sun"
if "Son" in txt5:
	print("'son' word is available.")
else:
	print("'son' word is unavailable.")


#Using 'in not' statement
txt6="Kali Linux is a shit"
print("kali" not in txt6)
var3="Kali" not in txt6
print(var3)

txt7="I love Huskies"
print("love" not in txt7)
var4="LOVE" not in txt7
print(var4)

#Using 'if not' statement
txt8="Keep you mind"
if "keep" not in txt8:
	print("'keep' word is unavailable.")
else:
	print("'keep' word is available.")

txt9="Let you suck"
if "Let" not in txt9:
	print("'Let' word is unavailable.")
else:
	print("'Let' word is available.")