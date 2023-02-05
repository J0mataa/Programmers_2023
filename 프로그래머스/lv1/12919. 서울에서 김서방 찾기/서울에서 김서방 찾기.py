def solution(seoul):
    #결론: 김서방의 위치 찾기
    cnt = 0 
    ans = 0
    
    for x in seoul:
        if x == "Kim":
            ans = cnt
        else:
            cnt+=1
            
    return (f"김서방은 {ans}에 있다")