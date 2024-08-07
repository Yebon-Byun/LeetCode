# Approach 1: DFS
# Time Comp: O(N + E) N is the number of rooms, and E is the total number of keys
# Space Comp: O(N)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        
        while stack:
            node = stack.pop()
            
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
                    
        return all(seen)