class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #1 Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return None
        
        #2 Two-pass HashTable
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         # 'hashmap[complement] != i -> In the line 13, 14, we'd insert
        #         # array 'nums' in to dict 'hashmap' and declare keys - random values
        #         # (through the iteration for using dict).
        #         # So, the key ' complement' must not be the values set up 
        #         # using iteration.
        #         return [i, hashmap[complement]]
        
        #3 One-pass HashTable
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            