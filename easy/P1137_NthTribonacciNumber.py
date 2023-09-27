# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class P1137_NthTribonacciNumber(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [0,1,1]    # create array to store tribonacci numbers
        
        for i in range(3,n+1):
            new = fib[i-1] + fib[i-2] + fib[i-3]  # keep adding numbers to array until we get our n
            fib.append(new)
        return fib[n]    # return the tribonacci value at index n
