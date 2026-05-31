n = 122
summation = 0

while n != 0:
    temp = n % 10
    summation += temp
    n //= 10
    
print(summation)
