# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class P844_BackspaceStringCompare:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ""
        b = ""                            # placeholder for final str

        for i in range(len(s)):
            if s[i] == "#":
                a = a[:-1]
            else:
                a = a + s[i]              # deduce actual s str
        
        for i in range(len(t)):
            if t[i] == "#":
                b = b[:-1]
            else:
                b = b + t[i]              # deduce actual t str
        
        return (a == b)                   # compare
            
