print("7-6. 20203035 김석준\n")

fruit_list =['banana', 'orange', 'kiwi', 'apple', 'melon']
pop_fruit = []
print(fruit_list)
length = 0

for i in fruit_list:
    if length < len(i):
        length = len(i)

        
for i in range(len(fruit_list) - 1, -1, -1):
    if len(fruit_list[i]) == length:
        pop_fruit.append(fruit_list[i])
        fruit_list.pop(i)

pop_fruit.sort()
print(pop_fruit)
print(fruit_list)
