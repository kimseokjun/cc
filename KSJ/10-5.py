import numpy as np

print("10-5. 20203035 김석준")
players = [[170, 76.4, 24],[183, 86.2, 24], [181, 78.5, 25],[176,80.1,26]]

np_players=np.array(players)

print("몸무게가 80 이상인 선수 정보")
print(np_players[np_players[:,1]>= 80.0])

print("키가 180이상인 선수 정보")
print(np_players[np_players[:,0]>= 180.0])

print("나이가 25이상인 선수 정보")
print(np_players[np_players[:,2]>= 25])
