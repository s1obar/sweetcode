package easy.java;

public class Main {
    public static void main(String[] args){
        int[] array = new int[]{-1,1,0,-3,3};
        int[] result = ProductOfArrayExceptSelf.productExceptSelf(array);
        for(int i : result){
            System.out.println(i);
        }
    }
}
