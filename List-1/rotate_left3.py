def rotate_left3(nums):
  first = nums[0]
  nums.pop(0)
  nums.append(first)
  return nums
