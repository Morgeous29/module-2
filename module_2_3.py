my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
while index < len(my_list):
    x = my_list[index]
    index += 1
    if x == 0:
        continue
    elif x < 0:
        break
    elif index == len(my_list):
        print(x)
    else:
        print(x)
