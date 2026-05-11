nums = [1,34,7]
digit = 9
d_count = 0

for i in nums:
    while i != 0:
        rem = i % 10
        i //= 10
        if rem == digit:
            d_count += 1
            
print(d_count)