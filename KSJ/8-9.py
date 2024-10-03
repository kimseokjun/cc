print("8-9.    20203035 김석준\n")



student_tup = (('211101', '최성훈', '010-1234-4500'),
               ('211102', '김은지', '010-2230-6540'),
               ('211103', '이세은', '010-3232-7788') )

student_dic = {}
for x in range(len(student_tup)):
    num, name, phone = student_tup[x]
    name_phone = [name,phone]
    student_dic[num] = name_phone


student_dic["211101"].append(4.3)
student_dic["211102"].append(3.9)
student_dic["211103"].append(4.25)

print("학생의 정보 목록")
for key,value in student_dic.items():
    print("{","'",key,"'", ":", value,"}")

result = 0
for value in student_dic.values():
    result +=value[2]

print("전체 학생의 학점 평균 : {:.2f}". format(result/3.0))
