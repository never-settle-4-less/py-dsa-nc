from typing import List


def disallow_negatives(num: int) -> int:
    return max(0, num)


# max_diff = ?

# for every adjacent pair:
#     diff = nums[i] - nums[i - 1]

#     if diff > max_diff:
#         update max_diff

# return max_diff


def max_difference(nums: List[int]) -> int:

    max_diff = nums[1] - nums[0]

# Since differences can be negative, initializing to 0 can be risky in general.
# Best approach:
# Initialize using the first valid difference.
# Something like mentally:
# max_diff = nums[1] - nums[0]
# Why this is good:
# guarantees a real comparison value
# works for negative and positive cases
# avoids arbitrary initialization
    
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
    
    return max(diff, max_diff)



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
