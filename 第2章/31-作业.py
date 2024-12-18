# 给定一个整数列表，找出列表中两个元素的和等于目标值的所有组合。
nums = [2, 4, 6, 8, 10]
target = 12

nums.sort()
left = 0
right = len(nums) - 1
result = []

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        result.append([nums[left], nums[right]])
        left +=1
        right -=1
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(result)