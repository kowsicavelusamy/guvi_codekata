print("enter the numbers")
i=input()
j=input()
k=input()
if(i<j):
    if(j>k):
        print("{0} is larger".format(j))
    elif(k>i):
        print("{0} is larger".format(k))
elif(i>k):
    print("{0} is larger".format(i))

