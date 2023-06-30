# TODO: Declare global variables here.
recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    # Type your code here.
    global recursions, comparisons

    # Increment the number of recursive calls
    recursions += 1

    # Calculate the index midway between lower and upper bounds
    index = (lower + upper) // 2

    # Increment the number of target comparisons
    comparisons += 1

    # Check if the target is found at the current index
    if target == nums[index]:
        return index

    # Check if lower and upper bounds are the same (not found)
    if lower == upper:
        return -1

    # Make recursive calls based on target and current index
    if nums[index] < target:
        comparisons += 1
        return binary_search(nums, target, index + 1, upper)
    else:
        comparisons += 1
        return binary_search(nums, target, lower, index - 1)

if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]
    
    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
