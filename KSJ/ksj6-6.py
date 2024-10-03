def fibonacci(n):
    count =0
    if n <2:
        return n
    a,b = 0,1
    for i in range(n -1):
        a,b = b, a+b
        count = count +1
    return b,count

while True:
    i = int(input("몇 번째 항 : "))
    val, count= fibonacci(i-1)
    print(val)
    print('count=', count)
