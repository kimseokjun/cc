print("8-4.    20203035 김석준")

partyA = set(["Park","Kim", "Lee"])
partyB = set(["Park","Choi"])

print("파티 A,B에 참석한 사람들 : ", end=" ")
for x in partyA.union(partyB):
    print(x, end=" ")
print()
print("파티 A에 중복없이 참석한 사람들 : " , end=" ")
for x in partyA.symmetric_difference(partyB):
    print(x, end=" ")
print()
print("파티 A에 참석한 사람들 : ", end=" " ) 
for x in partyA.difference(partyB):
    print(x, end=" ")

