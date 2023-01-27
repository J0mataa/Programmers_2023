def solution(n):
    # 정수 쪼개기
    sort_list = list(str(n)) #정수 --> 문자열 변환 --> 리스트로 하나씩 자름
    print(sort_list)
    ans = ''
    
    
    # 버블정렬 Bubble sort
    for x in range(len(sort_list)): #큰 회차
        for i in range(len(sort_list)-1):
            #비교
            if sort_list[i] < sort_list[i+1]: #뒤가 더 크면?
                #앞과 위치 변경
                sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
                
            else: #앞이 크면?
                pass #유지
    
    
    # 리스트값 --> 문자열 --> int로(정수로)
    for x in sort_list:
        ans+=x
    ans = int(ans)
    
    
    
    return ans