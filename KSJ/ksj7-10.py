print("7-10. 20203035 김석준\n")



def overlap(A,B):
    result = A[:]
    for i in range(len(B)):
        if(B[i] not in A):
            result +=B[i]
    return result
            


while True:
    list1 = input("문자열1을 입력하시오 : ")
    list2 = input("문자열2을 입력하시오 : ")
    if(list1== '' and list2==''):
        break
    result = overlap(list1,list2);
    print(result)
