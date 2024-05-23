​python splicing

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numsp[3:(끝까지)]) # Output: [3, 4, 5, 6, 7, 8, 9]

# Slice from the beginning to index 3 (excluding 3)
print(nums[(처음부터):3])  # Output: [0, 1, 2]

# Slice the last 3 elements
print(nums[-3:(끝까지)])  # Output: [7, 8, 9]

# Slice all elements except the last 2
print(nums[(처음부터):-2])  # Output: [0, 1, 2, 3, 4, 5, 6, 7]