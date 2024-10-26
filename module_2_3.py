my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

positive_numbers = []
index = 0

while index < len(my_list):
    if my_list[index] > 0:
        positive_numbers.append(my_list[index])
        index += 1
    elif my_list[index] == 0:
        index += 1
    else:
        break

index = 0
while index < len(positive_numbers):
    print(positive_numbers[index])
    index += 1
    continue
    break