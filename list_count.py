NameList = ['ye','kill','red',1,2,5,3,'jjl',99,2,'jjl',2]
i = 0
j = NameList[-1]
while NameList.count(j) != 1:
    NameList.remove(j)
    i += 1
else:
    k = NameList.index(j)
print ("Your namelist  length :%s"%(i+k+1))