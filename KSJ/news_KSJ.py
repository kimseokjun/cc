stadium = input("오늘의 축구경기장은 어디입니까?")
HOME_TEAM = input("오늘의 홈팀은 어디입니까?")
AWAY_TEAM = input("오늘의 어웨이팀은 어디입니까?")
FAVORITE_TEAM = input("당신이 좋아하는 팀은 어디입니까?")
FAVORITE_PLAYER = input("당신이 좋아하는 선수는 누구입니까?")

print("")
print("==========================================")
print("오늘은 {}에서 {}팀과 {}팀의 경기가 있는 날입니다.".format(stadium,HOME_TEAM,AWAY_TEAM))
print("축구경기를 보러온 김석준 학생과 인터뷰를 나누어보도록 하겠습니다.")
print("안녕하세요 제가 좋아하는 팀은 {}입니다.".format(FAVORITE_TEAM))
print("이번경기에서 {} 선수가 해트트릭을 했으면 좋겠습니다.".format(FAVORITE_PLAYER))
print("==========================================")
