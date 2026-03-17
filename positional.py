def add(a,b):
    print("a=",a)
    print("b=",b)
    print("b=",b)
    return a+b
result=add(2,5)
print("sum=",result)

def student_info(name,roll,marks):
    print("name:",name)
    print("roll:",roll)
    print("marks:",marks)
student_info("ravi",101,85)

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print(p*r*n)/100
    simple_interest(10000,2,2)
    simple_interest(50000,1.2,3)

def ar_circle(r):
    ar_circle=3.14*r*r
    print("area of circle:",ar_circle)
ar_circle(1.5)
ar_circle(4)


def check_value (no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(90)
check_value(-15)


def even_odd(no):
    if(no%2==0):
        print("even")
    else:
        print("odd")
even_odd(50)
even_odd(15)

def addition (a,b):
    add=a+b
    print("addition of two value:",add)
addition(50,10.5)
addition(100,200)