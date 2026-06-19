nums = [3, 7, 1, 9, 4]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n
print(f"Max: {max_val}")  