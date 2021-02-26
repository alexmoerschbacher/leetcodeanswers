def numJewelsInStones(jewels, stones):
    counter = 0
    for stone in stones:
        if stone in jewels:
            counter += 1
    return counter
