import random

def get_code():
    numbers = list(range(3, 21))
    code = random.choice(numbers)
    return code

n = get_code()
print('Шифр:', n)

def get_passcode(n):
    passdict = {}
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
                     10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
                     14: 1611325212343114105968, 15: 1214114232133124115106978,
                     16: 1317115262143531341251161079, 17: 11621531441351261171089,
                     18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
                     20: 13141911923282183731746416515614713812911})
    passcode = passdict.get(n)
    return passcode

num1 = list(range(1, n))
num2 = list(range(1, n))
result = ''

for i in num1:
    for j in num2:
        if i >= j:
            continue
        else:
            if n % (i + j) == 0:
                result = result + str(i) + str(j)
print('Пароль:', result)