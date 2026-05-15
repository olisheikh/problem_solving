n = 5

count = 0
l2 = []
for i in range(n+ 1):
    n2 = i 
    while n2 != 0:
        count += n2 % 2
        n2 = n2 // 2
        
    l2.append(count)
    count = 0
    
print(l2)