a = list(map(int, input().split()))
for number in a:
    if number % 2 == 0:
        print(number, end=' ')
    elif number == 237:
        break