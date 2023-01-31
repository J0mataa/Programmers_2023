a, b = map(int, input().strip().split(' '))

#한 줄의 별은 a만큼 / *b만큼

for x in range(b):
    print(a*'*')