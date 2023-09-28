class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Approach 1: Compare with Reverse
        
        We'll reverse the given string and compare it with the original, if those are
        equivalent, it's palindrome.
        
        Since only alphanumeric characters are considered, we'll filther out all other
        types of characters before we apply our algorithm.
        
        Additionally, because we're treating letters as case-sensitive, we'll convert
        the remaining letters to lower case. The digits will be left the same.
        
        Approach 2: Two Pointers
        
        every palindrome half is reverse of the other half.
        If one traverse outwards in the middle of a palindrome, it would encouter 
        the same characters in the exact same order, in both halves.
        """
        
        #1
        
        # filtered_chars = filter(lambda ch:ch.isalnum(), s)
        # lowercase_filtered_chars = map(lambda ch:ch.lower(), filtered_chars)
        # filtered_chars_list = list(lowercase_filtered_chars)
        # print("filtered_chars_list : ", list(filtered_chars_list))
        # reversed_chars_list = filtered_chars_list[::-1]
        # print("reversed_chars_list : ", reversed_chars_list)
        # return filtered_chars_list == reversed_chars_list
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        #2
        i = 0
        j = len(s) - 1
        
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
                
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            
        return True
        