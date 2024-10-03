while True:
    count = 0
    word = input("단어를 입력하세요 : ")
    print(word)
    for i in word:
        if i in [ 'a' ,'e', 'i', 'o' ,'u','A','E','I','O','U']:
            count +=1
            
    print("모음의 개수는 {}개 입니다.".format(count))
        
