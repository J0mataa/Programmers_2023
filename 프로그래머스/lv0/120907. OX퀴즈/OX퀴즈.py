def solution(quiz):
    #1. quiz[0]을 꺼낸다.
    #2. 쪼갠다.
    #3. 다시 꺼내서 계산한다
    #4. 정답리스트에 답안O/X를 넣는다.
    
    #연산자는 +or-
    
    ans = [] #답안제출용
    quiz_sp = [] #퀴즈 쪼갠거
    
    for x in range(len(quiz)):
        quiz_sp = quiz[x].split(" ") #퀴즈쪼갬

        if quiz_sp[1]=='-': # -일 경우
            if int(quiz_sp[0]) - int(quiz_sp[2]) == int(quiz_sp[4]):
                ans.append('O')
            else:
                ans.append('X')
        else: # +일 경우
            if int(quiz_sp[0]) + int(quiz_sp[2]) == int(quiz_sp[4]):
                ans.append('O')
            else:
                ans.append('X')
                    
                    
    return ans