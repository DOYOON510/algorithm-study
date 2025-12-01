nums = input().split('-')

result = sum(map(int, nums[0].split('+')))
for part in nums[1:]:
    result -= sum(map(int, part.split('+')))

print(result)