print("8-5.    20203035 김석준")


def process(w):
    output=""
    for ch in w:
        if ch.isalpha():
            output +=ch
    return output.lower()

words = set()
list1 = []
fname = input("입력 파일 이름 : ")
file = open(fname,"r")
for line in file:
    lineWords = line.split()
    for word in lineWords:
        words.add(process(word))
        list1.append(process(word))

print("사용된 단어의 개수 = ", len(words))
print("중복된 단어의 개수 = ", len(list1)-len(words))
print(words)
