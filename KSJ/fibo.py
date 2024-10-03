def fibonacci(n):
    count =0
    if n <2:
        return n
    a,b = 0,1
    for i in range(n -1):
        a,b = b, a+b
        count = count +1
    return b,count
