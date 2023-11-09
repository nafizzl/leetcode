# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

# A string is homogenous if all the characters of the string are the same.

# A substring is a contiguous sequence of characters within a string.

class P1759_CountNumberofHomogenousSubstrings:
    def countHomogenous(self, s: str) -> int:
        homSub = 0
        i = 0
        j = 0                                       # counter for recording homogenous substrings and pointers
        
        while i < len(s) and j < len(s):
            if s[i] == s[j]:
                j += 1                              # increment if same character
            else: 
                homSub += ((j-i) * (j-i+1)) // 2    # use first n natural sum formula to add substrings
                i = j                               # adjust pointer for different character

        if j == i:
            homSub += 1                             # last character is different from previous
        else:
            homSub += ((j-i) * (j-i+1)) // 2        # last character is same as previous
            i = j
        
        return homSub % (10**9 + 7)
