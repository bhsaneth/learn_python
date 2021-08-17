#Practise Project 1 
#Discussion between a Shop owner and Customer

fruit="banana"
count=5
prize=50
own="owNER:"
cust="CUSTOMER:"
saying4="How much for this "
saying5="Each one is {} dollars"
saying6="Ok, I wanna buy {1} {0}s"
saying7="Then, total prize is {}"
saying8="Here...Good Day for you!"
saying9="You too..."

print(own[0].upper()+own[1]+own[2:].lower()+" "+saying4+" "+fruit+"?")
print(cust[0]+cust[1:].lower()+" "+saying5.format(prize)+saying9[7])
print(own[0].upper()+own[1]+own[2:].lower()+" "+saying6.format(fruit,count)+saying9[7])
print(own[0].upper()+own[1]+own[2:].lower()+" "+saying7.format(count*prize)+saying9[7])
print(cust[0]+cust[1:].lower()+" "+saying8)
print(own[0].upper()+own[1]+own[2:].lower()+" "+saying9)