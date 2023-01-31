def solution(n, numlist):
    ans = []
    for x in numlist:
        if x%n==0: #numlist값을 n으로 나눈 나머지값이 XX없으면
            #n의 배수
            ans.append(x)
        else:
            pass
        
    return ans