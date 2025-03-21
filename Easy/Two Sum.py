def two_sum(nums, target):
    """
    Finds indices of two numbers in the list 'nums' which add up to the 'target'
    Args:
        nums: A list of integers
        target: The target sum to achieve

    Returns:
        List[int]: A list containing the indices of the two numbers that add up to the target.
    """
    # Dictionary to store the value and it's corresponding index.
    nums_dict = {}

    #Iterate through the list with index and value
    for i, num in enumerate(nums):
        complement = target - num

        # If the complement is in the dictionary return the answer.
        if complement in nums_dict:
            return [nums_dict[complement], i]
        
        # If not add the number and index to the dictionary.
        nums_dict[num] = i

# Example usage:
nums = [2, 11, 15, 7]
target = 9
print(two_sum(nums, target))  # Output: [0, 2]