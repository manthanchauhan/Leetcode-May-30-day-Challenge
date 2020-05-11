class Solution {
    public int findJudge(int N, int[][] trust) {
        int[] arr = new int[N+1];
            
        for(int i = 1 ; i<=N ; i++){
            arr[i] = 0;
        }
        for(int i = 0 ; i< trust.length; i++){
            int u = trust[i][0];
            int v = trust[i][1];
            arr[u]--;
            arr[v]++;
        }
        
        for(int i = 1 ;  i<=N ; i++){
            if(arr[i] == N-1){
                return i;
            }
        }
        return -1;
    }
}