def kidsWithCandies(candies, extraCandies):
    boolList = []
    greatestCandies = 0
    for kid in candies:
        if greatestCandies < kid:
            greatestCandies = kid
        
    for kid in candies:
        if kid + extraCandies >= greatestCandies:
            boolList.append("true")
        else:
            boolList.append("false")
    return boolList
print(kidsWithCandies([2,3,5,1,3], extraCandies = 3))
        