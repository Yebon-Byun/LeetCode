class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Approach 1 : Simulation
        
        This is the most straightforward approach, but as we'll see soon, althogh it does
        pass here on Leetcode, it's not very efficeint and is not likely to get you a job
        at a top company.
        
        Approach 2: Two Hashmaps
        
        
        """
        #1
#         for c in ransomNote:
#             if c not in magazine:
#                 return False
            
#             location = magazine.index(c)
            
#             magazine = magazine[:location] + magazine[location + 1:]
                
        #2
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_counts = collections.Counter(magazine)
        # print("magazine_counts : ", magazine_counts)
        ransom_note_counts = collections.Counter(ransomNote)
        # print("ransom_note_counts : ", ransom_note_counts)
        # print("ransom_note_counts.items( ) : ", ransom_note_counts.items())
        
        for char, count in ransom_note_counts.items():
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
        
        return True
        
        
        # Approach 3 : One HashMap