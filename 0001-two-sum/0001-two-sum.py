class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         1 Brute force | O(n^2)
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return None
        
#         2 Two-pass HashTable | O(n)
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 # 'hashmap[complement] != i -> In the line 13, 14, we'd insert
#                 # array 'nums' in to dict 'hashmap' and declare keys - random values
#                 # (through the iteration for using dict).
#                 # So, the key ' complement' must not be the values set up 
#                 # using iteration.
#                 return [i, hashmap[complement]]
        
#         3 One-pass HashTable | O(n)
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i
        
        # 4 Two-pointer | 
        nums = [[n, i] for i, n in enumerate(nums)]
        # enumerate( )열거! enumerate object의 key 값을 부여해준다. 
        # The enumerate( ) function takes a collection and returns it as an enumerate object
        # n: 값 / i: 인덱스
        nums.sort(key=lambda x: x[0])
        l, r = 0, len(nums) - 1
        print('l :', l)
        print('r :', r)

        while l < r:
            num_sum = nums[l][0] + nums[r][0]
            if num_sum == target:
                return [nums[l][1], nums[r][1]]
            elif num_sum > target:
                r -= 1
            else:
                l += 1
        
    
