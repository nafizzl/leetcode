class P49_GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:              
        groups = defaultdict(list)                                          # use defaultdict class, a subclass of dictionaries for easy hashing
        for i in strs:                                                      # linear time checking anagrams
            groups["".join(sorted(i))].append(i)                            # the key will be the "pure anagram", so if a word is an anagram of another, it will have the same key and be added
        return list(groups.values())                                        # we use join since we want a string for the key, something that is hashable, a list is NOT hashable
        
    #     groups = {}                                                       # similar approach but had to convert sorted character strings to tuples for hashability
    #     groups[tuple(sorted(strs[0]))] = [strs[0]]

    #     for i in range(1, len(strs)):
    #         if tuple(sorted(strs[i])) in groups:
    #             groups[tuple(sorted(strs[i]))].append(strs[i])
    #         else:
    #             groups[tuple(sorted(strs[i]))] = [strs[i]]

    #     return list(groups.values())

        
        # output = [[]]                                                     # an O(n^2) algorithm that works, but runs for a long time
        # output[0] = [strs[0]]
        # for i in range(1, len(strs)):
        #     for j in range(len(output)):
        #         if sorted(strs[i]) == sorted(output[j][0]):
        #             output[j].append(strs[i])
        #             break
        #         if j == len(output) - 1:
        #             output.append([strs[i]])
        # return output
