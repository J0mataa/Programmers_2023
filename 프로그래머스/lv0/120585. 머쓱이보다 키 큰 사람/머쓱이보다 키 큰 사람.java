class Solution {
    public int solution(int[] array, int height) {
        int cnt = 0; //머쓱이보다 큰 사람의 수
        
        for(int i=0; i<array.length; i++){ // array값 꺼내기 용
            if(height<array[i]){ // 머쓱이보다 큰 사람 비교
                cnt+=1; //크면? --> cnt추가
            }
        }
        
        return cnt;
    }
}