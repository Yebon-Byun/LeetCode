# MY OWN
# I wasn't sure how to utilize the parantheses as a key point resolving this problem
# class Solution:
#     def decodeString(self, s: str) -> str:
#         p = 0
#         temp_str = ""
#         temp_num = 0
#         n_list = deque()
        
#         for i in reversed(s):
#             if i == ']':
#                 p -= 1
#             elif i == '[':
#                 p += 1
#             elif i.isalpha() and p < 0:
#                 temp_str = i
#                 n_list.appendleft(i)
#             elif i.isdigit() and p < 0:
#                 temp_num = i
#                 n_list.appendleft(int(temp_num) * temp_str)
#             elif i.isdigit():
#                 temp_num = i    
#                 n_list.appendleft(int(temp_num) * temp_str)
#             elif i.isalpha():
#                 temp_str = i
#         return ''.join(n_list)

# Approach: Stack
# Time Comp: O(n)
# Space Comp: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        curr_num = 0
        res = ""
        stack = []
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append(curr_num)
                stack.append(res)
                curr_num = 0
                res = ""
            elif c == ']':
                res = stack.pop() + res * stack.pop()
            else:
                res += c
            
        return res

                