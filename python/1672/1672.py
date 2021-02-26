def maximumWealth(accounts):
    highestSum = 0
    for person in accounts:
        if sum(person) > highestSum:
            highestSum = sum(person)
    return highestSum

print(maximumWealth([[1,5],[7,3],[3,5]]))
