/*
Problem 1: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
  */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer; // instantiate a vector to hold the answers
        for (int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++){ // this solution implements nested loops for O(n^2) runtime
                if (nums.at(i) + nums.at(j) == target) {
                    answer.clear();  
                    answer.push_back(i);
                    answer.push_back(j);  // clear whatever's inside the answer vector and replace with the new answers
                }
            }
        }
        return answer;
    }
};
