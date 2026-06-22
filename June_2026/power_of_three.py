num = 27
is_power = False
for i in range(1, num):
    temp = 3 ** i 
    
    if temp <= num:
        if num == temp:
            is_power = True
            break
    else:
        break
        
print(is_power)