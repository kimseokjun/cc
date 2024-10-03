print("8-7.    20203035 김석준\n")



student_tup = (('211101', '최성훈', '010-1234-4500'),
               ('211102', '김은지', '010-2230-6540'),
               ('211103', '이세은', '010-3232-7788') )

student_dic = {}
for x in range(len(student_tup)):
    num, name, phone = student_tup[x]
    name_phone = [name,phone]
    student_dic[num] = name_phone


num = input("학벅을 입력하시오 : ")
print("이름 : {}".format(student_dic[num][0]))
