def solution(n, t): #n은 마리 수 / t는 경과한 시간
    
    
    #기본값n = 2
    #1시간 --> n=n*2 / 2배증가
    
    for x in range(t):
        n*=2 #1시간당 2배씩 늘어남
        
    return n
    