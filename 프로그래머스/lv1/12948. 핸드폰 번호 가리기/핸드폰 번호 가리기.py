def solution(phone_number):
    answer = ''
    
    answer += (len(phone_number)-4)*'*' #뒷자리 수 4자 빼고 나머지 *
    answer += phone_number[len(phone_number)-4:] #나머지 4글자 넣기
    
    
    return answer