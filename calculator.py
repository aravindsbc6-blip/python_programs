a=int(input("enter first number = "))
b=int(input("enter second number = "))
op=input("oprator = ")
if op=="+":
    sum=a+b
    print(sum)
elif op=="*":
    c=a*b
    print(c)
elif op=="-":
    c=a-b
    print(c)
elif op=="/":
    try:
        c=a/b
    except ZeroDivisionError:
        print("can't divide by zero")    
    print(c)
else:
    print("not defined oprator")