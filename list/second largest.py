nums = [3, 7, 1, 9, 4, 6]
largest = second = nums[0]
for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n
print("Second Largest:", second)  