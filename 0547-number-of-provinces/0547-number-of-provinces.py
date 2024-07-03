# Approach 1: DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        
        if not isConnected:
            return 0
        
        def dfs(u):
            for v in range(n):
                if isConnected[u][v] == 1 and visited[v] == False:
                    visited[v] = True
                    dfs(v)
                    
        for idx in range(n):
            if visited[idx] == False:
                count += 1
                visited[idx] == True
                dfs(idx)
                
        return count
            
        