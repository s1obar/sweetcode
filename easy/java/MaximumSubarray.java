package easy.java;

public class MaximumSubarray {
    public static int maxSubArray(int[] array){
        int maxSub = array[0];
        int curSum = 0;

        for(int n : array){
            if(curSum < 0){
                curSum = 0;
            }
            curSum += n;
            maxSub = Math.max(maxSub, curSum);
        }

        return maxSub;
    }
}
