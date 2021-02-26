icounter = 0
jcounter = 0
pairs = 0
nums = [1,2,3,1,1,3]
for i in nums:
    for j in nums:
        if i == j and icounter != jcounter and icounter < jcounter:
            pairs += 1
        jcounter += 1
    icounter += 1
    jcounter = 0
print(pairs)