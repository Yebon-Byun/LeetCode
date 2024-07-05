# MY OWN
# FAIL, I thought this in a wrong way. I found this simple as it would be good if I could compare the values and check the directions are changed
# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         len_n = len(connections)
#         visited = [False] * len_n
#         ans = 0
        
#         def dfs(current):
#             nonlocal ans
#             comp_list = []
            
#             for inside_iter in range(2):
#                 comp_list.append(connections[current][inside_iter])
#                 print(comp_list)
                
#             if comp_list[0] < comp_list[1]:
#                 ans += 1
#             else:
#                 comp_list = []
                
#         for outer_iter in range(len_n):
#             if visited[outer_iter] == False:
#                 visited[outer_iter] = True
#                 dfs(outer_iter)
                
#         return ans
            
# Approahc 1: BFS(Breadth First Search)
# Time Comp: O(n)
# Space Comp: O(n)
# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         paths = defaultdict(list)
#         for src, dest in connections:
#             paths[src].append((dest, True))
#             paths[dest].append((src, False))
#         ans = 0
#         q = deque([0])
#         capital_network = set()
#         while q:
#             city = q.popleft()
#             capital_network.add(city)
#             # print(capital_network)
#             for connected_city, is_dest in paths[city]:
#                 if connected_city not in capital_network:
#                     q.append(connected_city)
#                     if is_dest:
#                         ans += 1
#         return ans


# Approach 2 : DFS
# Time Comp : O(n)
# Space Comp: O(n)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # Create a graph with directional edges and their respective flags
        paths = defaultdict(list)
        for src, dest in connections:
            paths[src].append((dest, True))
            paths[dest].append((src, False))
        
        def dfs(city):
            capital_network.add(city)
            for connected_city, is_dest in paths[city]:
                if connected_city not in capital_network:
                    if is_dest:
                        self.ans += 1
                    dfs(connected_city)
        
        # Initialize
        self.ans = 0
        capital_network = set()
        
        # Start DFS from the capital city 0
        dfs(0)
        
        return self.ans
