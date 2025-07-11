"""
Input: stones = [2,7,4,1,8,1] 
Output: 1

1, 1, 2, 4, 7, 8
-> 1, 1, 1, 2, 4
-> 1, 1, 1, 2
-> 1, 1, 1
-> 1
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x-y)
        stones.append(0)
        return abs(stones[0])


