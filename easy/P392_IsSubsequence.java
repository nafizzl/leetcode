/*
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
*/

class P392_IsSubsequence {
    public static boolean isSubsequence(String s, String t) {
        char[] firstString = s.toCharArray();
        char[] secondString = t.toCharArray();
        int match = 0;          // convert strings to character arrays to compare and initialize counetr for number of matches
        

        int i = 0; 
        int j = 0;
        while (j < secondString.length && i < firstString.length) {
            if (firstString[i] == secondString[j]) {
                  match++;
                  i++;
               }
               j++;
            }                     // this loop allows us to match characters and do it while in order            
          
        if (match == firstString.length) {
        return true;             // if the counter equals the length of the subsequence, meaning it matched all characters, it's true
        }
        else {
        return false;            // otherwise false
        }
     }

}
