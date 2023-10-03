# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class P1512_NumberofGoodPairs:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    good += 1
                    # nested for loop to check between pairs of numbers in array
        return good
