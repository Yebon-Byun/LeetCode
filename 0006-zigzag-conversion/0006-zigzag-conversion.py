# Approach 1: Simulate Zig-Zag Movement
# class Solution:
#     def convert(self, s: str, num_rows: int) -> str:
#         if num_rows == 1:
#             return s

#         n = len(s)
#         sections = ceil(n / (2 * num_rows - 2.0))
#         num_cols = sections * (num_rows - 1)

#         matrix = [[" "] * num_cols for _ in range(num_rows)]

#         curr_row, curr_col = 0, 0
#         curr_string_index = 0

#         # Iterate in zig-zag pattern on matrix and fill it with string characters.
#         while curr_string_index < n:
#             # Move down.
#             while curr_row < num_rows and curr_string_index < n:
#                 matrix[curr_row][curr_col] = s[curr_string_index]
#                 curr_row += 1
#                 curr_string_index += 1

#             curr_row -= 2
#             curr_col += 1

#             # Move up (with moving right also).
#             while (
#                 curr_row > 0 and curr_col < num_cols and curr_string_index < n
#             ):
#                 matrix[curr_row][curr_col] = s[curr_string_index]
#                 curr_row -= 1
#                 curr_col += 1
#                 curr_string_index += 1

#         answer = ""
#         for row in matrix:
#             answer += "".join(row)

#         return answer.replace(" ", "")

# Approach 2: String Traversal
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        
        answer = []
        n = len(s)
        chars_in_section = 2 * (num_rows - 1)
        
        for curr_row in range(num_rows):
            index = curr_row
            while index < n:
                answer.append(s[index])
                
                if curr_row != 0 and curr_row != num_rows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between
                    
                    if second_index < n:
                        answer.append(s[second_index])
                    
                index += chars_in_section
            
        return "".join(answer)
        