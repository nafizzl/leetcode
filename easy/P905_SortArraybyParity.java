// Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

// Return any array that satisfies this condition.

class P905_SortArraybyParity {
    public int[] sortArrayByParity(int[] nums) {
        int[] sorted = new int[nums.length];
        int even = 0;
        int odd = nums.length - 1; // make array to hold answer and make pointers for even and odd numbers
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                sorted[even] = nums[i];
                even++;
            }
            else {
                sorted[odd] = nums[i];
                odd--;
            }
        } // array figures out if the number is even/odd and places in proper place
        return sorted;       
    }
}
