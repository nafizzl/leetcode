// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

import java.util.HashMap;
import java.util.ArrayList;

class P229_MajorityElementII {
    public List<Integer> majorityElement(int[] nums) {
        int min = nums.length / 3;                            // helps find all elements that appear more than ceil(n/3) times
        List<Integer> ans = new ArrayList();                   // holds answer for problem
        HashMap<Integer, Integer> hash = new HashMap();      // will help keep track of occurrence
        for (int i = 0; i < nums.length; i++) {             // this for loop records every unique value's occurrence
            if (!hash.containsKey(nums[i])) {
                hash.put(nums[i], 1);                        // first occurrence of a number
            }
            else {
                hash.put(nums[i], hash.get(nums[i]) + 1);     // increment number of appearances
            }
        }
        Set<Integer> keys = hash.keySet();
        for (Integer key : keys) {                         // find all keys that appear > n/3 times using key set
            if (hash.get(key) > min) {
                ans.add(key);
            }
        }
        return ans;
    }
}
