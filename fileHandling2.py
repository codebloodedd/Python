fileWrite = open("file3.txt", "w")
fileWrite.write("Hello, I am Pratham Shah and my birthday is on 10th june")
fileWrite.close()

fileRead = open("file3.txt", "r")
li = list()
f = fileRead.read()
f = f.split()

for i in f:
    li.append(str(i))
    li.sort(key= lambda item: (item, len(item)))

print(li)

fileWrite2 = open("file4.txt", "w")
for i in range(len(li)):
    fileWrite2.write(str(li[i]))
    fileWrite2.write("\n")