# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

class P1662_CheckifTwoStringsAreEquivalent(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1str = ''
        word2str = ''                    # make two empty strings
        
        word1str = word1str.join(word1)  # apply .join() to iterables to automatically join characters
        word2str = word2str.join(word2)
        
        return (word1str == word2str)    # comparison helps return true or false
