def sum2(nums):
  if(len(nums) == 0):
    res = 0
  elif(len(nums) < 2):
    res = nums[0]
  else:
    res = nums[0] + nums[1]
  return res
