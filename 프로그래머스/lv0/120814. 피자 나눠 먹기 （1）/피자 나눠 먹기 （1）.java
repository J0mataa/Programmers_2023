class Solution {
    public int solution(int n) {
        // 피자는 7조각
        // n명이 1조각 이상 먹을때 필요한 피자의 수
        
        if(n%7>=1){
            return n/7+1;
        }else{
            return n/7;
        }
    }
}