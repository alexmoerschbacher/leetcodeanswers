def runningSum(nums):
    runningSum = []
    sumHolder = 0
    for num in nums:
        sumHolder = sumHolder + num
        runningSum.append(sumHolder)
    return runningSum
nums = [3, 1, 2, 10, 1]

runningSum(nums)
