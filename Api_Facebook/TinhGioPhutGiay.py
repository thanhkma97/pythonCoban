t = int(input("nhap so giay: "))
hour = (t//3600)%24
minute =(t%3600)//60
second = (t%3600)%60
print(hour,":",minute,":",second)

print("{0} : {1} : {2}".format(hour,minute,second))
