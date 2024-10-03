print("8-10.    20203035 김석준\n")

student_tuple = [('211101', '강이안', '010-123-1111'),
                 ('211102', '박동민', '010-123-2222'),
                 ('211103', '김수정', '010-123-3333')]

print("1. student_tuple 리스트 출력")
print(student_tuple)


print("2. student_tuple 딕셔너리 출력")
student_dic = {}
for student in student_tuple:
    number, name, phone = student
    student_dic[number] = [name,phone]

for key, value in student_dic.items():
    print(' ',key + " :",value[0])



print("3. 학번으로 조회 결과 출력")
number = input("학번을 입력하시오 : ")
print("{} 학생은 {}이며, 전화번호는 {}입니다.".format(number,student_dic[number][0],student_dic[number][1]))
