class P389_FindtheDifference(object):
    def findTheDifference(self, s, t):
        check = s
        checked = t
        check_List = list(s)
        checked_List = list(t) # convert strings to char arrays
        
        for x in range(len(check_List)):
            for y in range(len(checked_List)):
                if (check_List[x] == checked_List[y]):
                  check_List[x] = " "
                  checked_List[y] = " "        # mark "found" characters with empty string

        added = " "
        for z in checked_List:
            if (z != " "): 
                 added = z  # added will contain the extra char in t

        return added
        
