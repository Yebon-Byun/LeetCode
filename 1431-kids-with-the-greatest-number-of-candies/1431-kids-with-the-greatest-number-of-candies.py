class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n -> kids
        # candies -> an integer array
        # candies[i] ->candies the ith kid has
        # extraCandies
        
        maxCandies = max(candies) #5
        
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)
        return result