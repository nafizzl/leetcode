# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

class Solution:

    def customSortString(self, order: str, s: str) -> str:
        inOrder = []
        notOrder = []
        odr = list(order)      # do conversion to make comparisons easier

        for char in s:
            if char in order:
                inOrder.append(char)
            else:
                notOrder.append(char) # divide s into characters found in order and not found in order

        for char in order:
            if char not in inOrder:
                odr.remove(char)      # if there's more characters in order than s, this will get rid of char that don't need consideration
        
        inOdr = ''.join(odr)
        inOrder = ''.join(inOrder)              # make strings for sorted function
        def customKey(char):
            return order.index(char)            # make this custom key for sorting
        sortedOrder = sorted(inOrder, key=customKey) 
        result = ''.join(sortedOrder)
        result = result + ''.join(notOrder)     # combine sorted part from order with characters not in order, which can be appended anywhere

        return result

        


