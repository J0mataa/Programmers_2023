def solution(num):
    # 1이 될때까지 반복
    # 센다
    cnt = 0
    
    if num == 1: # 만약 주어진 수가 1일 경우
        return cnt # 0반환
    
    
    while num != 1: # 숫자가 1이 아니면 True(반복)
    
        if num%2==0: #짝수
            num = num//2
            cnt+=1
        else: #홀수
            num = num*3+1
            cnt+=1
        
        if cnt == 500:
            cnt = -1
            break
            
    return cnt