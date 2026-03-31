f=open("one.txt","w")
f.write("hello students\n")
f.write("welcome to python file handling\n")
f.write("learning is fun\n")
f.close()

f=open("one.txt","w")
lines=[
"python programming\n"
"file handling\n"
"error handling\n"
"exception handling\n"
]
f.writelines(lines)
f.close()


f=open("one.txt","a")
f.write("this line is added at the end.\n")
f.close()