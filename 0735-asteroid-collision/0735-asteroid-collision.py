# MY OWN
# FAIL, I wasn't aware of there were many edge cases. I kept getting wrong answers, running into unexpected edge cases.
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         left = 0
#         if asteroids[-1] < 0 and sum(asteroids) == 0:
#             return []
        
#         elif asteroids[-1] > 0 and sum(asteroids) == 0:
#             return asteroids
        
#         else:
#             for i in range(len(asteroids) -1 , -1, -1):
#                 if asteroids[i] < 0:
#                     left += asteroids[i]
                
#                 if left + asteroids[i - 1] <= 0:
#                     continue
                    
#                 if left + asteroids[i - 1] > 0:
#                     return asteroids[0:i]

# Approach: Stack
# Time Comp: O(n)
# Space Comp: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ans = []
        for c in asteroids:
            if c > 0:
                stack.append(c)
            else:
                while len(stack) > 0 and stack[-1] < abs(c):
                    stack.pop()
                if len(stack) == 0:
                    ans.append(c)
                else:
                    if stack[-1] == abs(c):
                        stack.pop()
            
        ans += stack
        return ans