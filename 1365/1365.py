def smallerNumbersThanCurrent(nums):
    array = []
    for num in nums:
        biggerthan = 0
        for j in nums:
            if num > j:
                biggerthan += 1
        array.append(biggerthan)
    return array
smallerNumbersThanCurrent([8,1,2,2,3])