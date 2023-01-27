def solution(arr): #arr은 배열

    
#본인풀이
    small = arr[0] #가장 작은값 저장용
    ans = []
    
    
    #작은 수 찾기
    for x in range(1,len(arr)): #0,1,2,3,4,5
        if small < arr[x]: 
            small = small
        else:
            small = arr[x]
            
    
    for x in arr:
        #작은 수 면? 패스
        if x==small:
            pass
        else:
            #넣어
            ans.append(x)
        
    if not ans: #리스트가 비었는지 확인
        ans.append(-1)
        return ans
    else:
        return ans

    
    
#min과 remove사용 (현재 적용 불가 --> -1처리가 없음)
    arr.remove(min(arr))
    return arr
        
        










