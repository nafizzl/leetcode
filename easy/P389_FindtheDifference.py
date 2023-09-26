class P389_FindtheDifference(object):
    def findTheDifference(self, s, t):
        check = s
        checked = t
        check_List = list(s)
        checked_List = list(t) // convert strings to char arrays

        counter1 = 0;
        counter2 = 0;
        while(counter1 < len(check_List)):
            while (counter2 < len(checked_List)):
                if (check_List[counter1] == checked_List[counter2]):
                    checked_List[counter2] = " "
                counter2 += 1
            counter1 += 1 # iterate through both arrays, if char in s is found in t, change to empty char, at the 
                          # end, there will be only one empty char left
        
        counter3 = 0
        added = " "
        while(counter3 < len(checked_List)):
            if (checked_List[counter3] != " "): 
                 added = checked_List[counter3]  # added will contain the extra char in t
            counter3 += 1

        return added
        
