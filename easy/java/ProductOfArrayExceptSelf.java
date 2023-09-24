package easy.java;

class ProductOfArrayExceptSelf {
    public static int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        for(int i = 0; i <= result.length - 1; i++){
            result[i] = 1;
        }

        int prefix = 1;
        int postfix = 1;

        for(int i = 0; i <= nums.length - 1; i++){
            result[i] = prefix;
            prefix *= nums[i];
        }

        for(int i = nums.length - 1; i >= 0; i--){
            result[i] *= postfix;
            postfix *= nums[i];
        }

        return result;
    }
}
