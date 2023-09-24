package easy.java;

import java.util.HashSet;

public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] array){
        HashSet<Integer> set = new HashSet<>();
        for(int n : array){
            if(set.contains(n)){
                return true;
            }
            set.add(n);
        }
        return false;
    }
}
