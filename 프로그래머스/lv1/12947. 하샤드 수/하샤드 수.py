def solution(x):
    #하샤드 수? 10
    # 10 --> 자릿수의 합으로 10이 나누어져야함
    # ex) 1+0 =1 이고, 10은 1로 나누어 떨어진다. == True

    digit_list = list(str(x)) #자릿수 리스트

    
    ans = 0
    for i in range(len(digit_list)): #일의 자릿수 + 십의자릿수 + 백의자릿수
        ans += int(digit_list[i])

        
    if x%ans == 0: #나누어 떨어진다.
        return bool(1) #Boolean == True(1) or False(0)
    else:
        return bool(0)