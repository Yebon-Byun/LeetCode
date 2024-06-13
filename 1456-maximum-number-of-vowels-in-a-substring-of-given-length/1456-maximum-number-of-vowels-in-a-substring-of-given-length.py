# MY OWN
# FAIL, I wasn't sure how to manage string types with a way of sliding window, but also how to convert the string type into the int type.

# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         vls_list = ['a', 'e', 'i', 'o', 'u']
#         dict_vls = {str: 0 for str in vls_list}
#         sub = s[:k]
#         total, comp = 0, 0
        
#         for i in sub:
#             if i in dict_vls:
#                 total += 1
#             else:
                
#         print(total)
        
# Approahch: Sliding Window
# Time Comp: O(n)
# Space Comp: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)    
        answer = count
        
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            answer = max(answer, count)
            
        return answer