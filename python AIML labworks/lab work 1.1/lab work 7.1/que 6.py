def sum_product(*nums):
    s = sum(nums)
    p = 1
    for n in nums:
        p *= n
    return s, p

print(sum_product(1, 2, 3, 4))

# sum :- 1+2+3+4  1*1*2*3*4=24  
# output is :-(10, 24)