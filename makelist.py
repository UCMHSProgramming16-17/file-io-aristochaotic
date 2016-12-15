file = open("list.txt", "w")

for i in range(1, 11):
    file.write("%s. %s \n" % (str(i), input("add the next line")))
    
file.close() 