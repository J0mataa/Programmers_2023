def solution(s):
    # 공백기준으로 단어 구분
    # 짝수는 대문자 / 홀수는 소문자
    # 문자열 --> 문자열
    
    ans = ''
    
    split_sen = s.split(' ') # ['try', 'hello', 'world']
    
    
    for sen in split_sen: #자른것 --> sen ['try']
        for length in range(len(sen)): # try[0], try[1], try[2] --> t, r, y
            if length%2==0: #짝수
                ans+=sen[length].upper()
            else:
                ans+=sen[length].lower()
                
                
        ans+=' ' #띄어쓰기 처리
        
    ans = ans[:-1] #마지막 띄어쓰기 삭제
    
    return ans #리턴