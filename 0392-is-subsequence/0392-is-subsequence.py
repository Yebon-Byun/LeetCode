class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        two strins : s, t
        return true if s is a subsequence of t, or false otherwise.
        
        a subsequence of string is a new string that is formed from the original string
        by deleting some(can be none) of the characters without disturbing the relative
        positions of the remaining characters.
        
        
        
        Approach 1 : Divide and Conquer with Greedy
        
        'divide and conquer' technique: reduece the problem down into subproblems
        with smaller scales recursively until the problem becomes small enougth
        to tackle with.
        
        cross out the matched characters from both string and then continue with 
        the maching.
        
        this implementations happen to comply with a tail recursion, which is a 
        runtime potimization technique that is supported in some programming languages
        such as C and C++
        
        
        
        Approach 2 : Two-Pointers
        
        We could further optimize the space complexity of the previous solutions, 
        by replacing the recursion with the iteration.
        
        progress on the matching of the characters.
        
        if we found a match, we move left, right pointers one step forward.
        if no match is found, we move on ly the right pointer on ther target string.
        
        
        
        Approach 3 : Greedy Match with Character Indices Hashmap
        
        'bottleneck'
        scanning the target string through lookup operation in the array data structure.
        hashmap come in handy, since it has a O(1) time complexity for its lookup
        operation
        
        
        
        """
        
        #1
#         LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
        
#         def rec_isSubsequence(left_index, right_index):
#             if left_index == LEFT_BOUND:
#                 return True
#             if right_index == RIGHT_BOUND:
#                 return False
#             if s[left_index] == t[right_index]:
#                 left_index += 1
#             right_index += 1
#             return rec_isSubsequence(left_index, right_index)
#         return rec_isSubsequence(0, 0)
        
        #2
#         LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
#         p_left = p_right = 0
        
#         while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
#             if s[p_left] == t[p_right]:
#                 p_left += 1
#             p_right += 1
#         return p_left == LEFT_BOUND

        #3
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)
        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False
            
            indices_list = letter_indices_table[letter]
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False
        return True
        
            
        
        
            