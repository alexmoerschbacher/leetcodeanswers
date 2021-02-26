def shuffle(nums, n):
    counter = 0
    pairs = []
    arrayX = nums[:n] #First Half
    arrayY = nums[n:] #Last Half
    for x in arrayX:
        pairs.append(x)
        pairs.append(arrayY[counter])
        counter += 1
    return pairs
shuffle(nums, 3)