print("Enter 5 numbers:")
list1=list()
fileWrite=open("file1.txt","w")
for i in range(5):
    x=int(input(f"Enter number {i+1}: "))
    list1.append(x)
    fileWrite.write(str(list1[i]))
    fileWrite.write("\n")

fileWrite.close()

fileRead=open("file1.txt","r")
list2=list()

for j in fileRead:
    list2.append(int(j))
   
list2.sort()
fileWrite2=open("file2.txt","w")

for k in list2:
    fileWrite2.write(str(k))
    fileWrite2.write("\n")

fileWrite2.close()

fileRead2=open("file2.txt","r")

for x in fileRead2:
    print(x)
