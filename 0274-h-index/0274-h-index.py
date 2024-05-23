# MY OWN

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         arr = citations
#         arr.sort(reverse=True)
#         for index, value in enumerate(arr, start=1):
#             if index == value:
#                 return index
            
        
# Approach #1 Sotring

# Approach : Sorting and iteration Frequency
# Time : O(n log n) due to sorting
# Space : O(1)

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         n = len(citations)
#         citations.sort()
        
#         for i, v in enumerate(citations):
#             if n - i <= v:
#                 return n - i
#         return 0
    

#Approach #2 Counting

# Approach : counting and backward iteration
# Time : O(n)
# Space : O(n)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]
        
        for i, v in enumerate(citations):
            if v > n:
                temp[n] += 1
            else:
                temp[v] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i
        
        
                
           
            
        
        