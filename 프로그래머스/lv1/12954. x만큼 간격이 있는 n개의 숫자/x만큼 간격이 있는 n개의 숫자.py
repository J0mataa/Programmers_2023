def solution(x, n): #x씩 증가 , n는 회차
    ans = [] #정답 리턴용
    cnt = 0 #중간 저장용
    
    for i in range(n): #n만큼 반복
        cnt+=x #계속해서 값을 더해줌
        ans.append(cnt) #정답 리스트에 추가
    
    return ans #리턴