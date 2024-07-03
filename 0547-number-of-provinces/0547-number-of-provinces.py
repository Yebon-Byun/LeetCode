# Approach 1: DFS
# Time Comp: O(n^2)
# Space Comp: O(n)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        
        if not isConnected:
            return 0
        
        def dfs(current):
            for neighbor in range(n):
                if isConnected[current][neighbor] == 1 and visited[neighbor] == False:
                    visited[neighbor] = True
                    dfs(neighbor)
                    
        for idx in range(n):
            if visited[idx] == False:
                count += 1
                visited[idx] = True
                dfs(idx)
                
        return count
    
# Approach 2: BFS
# Time Comp: O(n^2)
# Space Comp: O(n)

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         visited = [False] * n
#         count = 0
        
#         def bfs(start):
#             queue = deque([start])
#             while queue:
#                 current = queue.popleft()
#                 for neighbor in range(n):
#                     if isConnected[current][neighbor] == 1 and not visited[neighbor]:
#                         visited[neighbor] = True
#                         queue.append(neighbor)
        
#         for idx in range(n):
#             if not visited[idx]:
#                 count += 1
#                 visited[idx] = True
#                 bfs(idx)
                
#         return count


            
        