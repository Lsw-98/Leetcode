n, k = map(int, input().split())
nums = [i for i in range(1, n + 1)]
num = 0
while len(nums) > 1:
    num = (k - 1 + num) % len(nums)
    del nums[num]
print(nums[0])
