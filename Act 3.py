def square(s,e):
    lst=[]

    for i in range(s,e):
        lst.append(i**2)

    even=[]
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    print("Even square:",even)
    print("Odd square:",odd)

square(1,10)