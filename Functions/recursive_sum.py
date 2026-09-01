def sum(nums):
    """Return the sum of the given numbers using recursion."""
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    
    else:
        return nums[0] + sum(nums[1:])

nums = [2, 9, 8, 76, 53]
result = sum(nums)  
print(result)  # Output: 148    
    