height = float(input("키를 입력하세요(cm) : "))
weight = float(input("몸무게를 입력하세요(kg) : "))
BMI = weight / (height*0.01)**2
print("당신의 BMI는 {}입니다".format(BMI))
