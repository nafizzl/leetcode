# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

class P1758_MinimumChangesToMakeAlternatingBinaryString:
    def minOperations(self, s: str) -> int:
        startZero = 0
        startOne = 0              # there are only two possible ways this alternating string can occur

        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '0':
                startZero += 1
            elif i % 2 == 1 and s[i] != '1':
                startZero += 1    # pattern 1: 01010101...
        
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '1':
                startOne += 1
            elif i % 2 == 1 and s[i] != '0':
                startOne += 1     # pattern 2: 10101010...
        
        return min(startZero, startOne)    # compare which one needs less steps
