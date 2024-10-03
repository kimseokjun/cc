count = 0

def fibonacci(n):
    global count
    count += 1
    if n < 0:
        print("잘못된 입력입니다.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

    
while True:
    i = int(input("몇 번째 항 : "))
    print(fibonacci(i))
    print("count = ", count)
    count = 0
