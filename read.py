f=open("one.txt","r")
d=f.read()
print("file content:",d)
f.close()


f=open("one.txt","r")
e=f.read(10)
print("first part:",e)
f.close()


f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line1:",line1)
print("line2:",line2)
print("line3:",line3)
f.close()

f=open("one.txt","r")
d=f.readlines()
print("list of lines:",d)
print("number of lines:",len(d))
f.close()


f=open("one.txt","r")
d=f.readlines()
print(d[1].strip())
f.close()



