class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Approach 1 : Simulation
        
        This is the most straightforward approach, but as we'll see soon, althogh it does
        pass here on Leetcode, it's not very efficeint and is not likely to get you a job
        at a top company.
        
        
        
        Approach 2: Two Hashmaps
        
        Count up how many of each letter are inboth the magazine and the ransome note.
        We can represent the counts with a HashMap, that has characters as keys, and
        counts as values.
        
        We can make two HashMaps; one for the magazine, and the other for the ransome
        note.
        
        Then, to check whether or not the ransom note can be made using the magazine, we 
        should loop over each character of the ransom note, checking how of it we need, 
        and checking that at least that many exist in the magazine, by lokking it up in
        the magazine HashMap.
        
        
        
        Approach 3 : One Hashmap
        
        A slightly better way than the second solution.
        we can simply put the magazine into a hashMap, and then substract characters
        from the ransom note form it.
        """
        #1
#         for c in ransomNote:
#             if c not in magazine:
#                 return False
            
#             location = magazine.index(c)
            
#             magazine = magazine[:location] + magazine[location + 1:]
                
    
    
        #2
#         if len(ransomNote) > len(magazine):
#             return False
        
#         magazine_counts = collections.Counter(magazine)
#         print("magazine_counts : ", magazine_counts)
#         ransom_note_counts = collections.Counter(ransomNote)
#         print("ransom_note_counts : ", ransom_note_counts)
#         print("ransom_note_counts.items( ) : ", ransom_note_counts.items())
        
#         for char, count in ransom_note_counts.items():
#             #char: 'a'
#             #count: 1
#             #ransom_note_coutns.items( ): dict_items(['a', 1])
#             #ransom_note_coutns.items( ) helps collection module to utilize as dictionary option
#             magazine_count = magazine_counts[char]
#             if magazine_count < count:
#                 return False
        
#         return True
        
        
        #3
        if len(ransomNote) > len(magazine):
            return False
        
        letters = collections.Counter(magazine)
        
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
            
        return True