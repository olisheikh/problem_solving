num = 3
t = 2
temp = 0
output = 1

while True:
    temp = (num + t) + output
    
    if (num + t) - output == num:
        print(temp)
        break 
    output += 1