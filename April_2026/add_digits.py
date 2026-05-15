def add_digit():
    num = 0
    
    while num != 0:
        num1 = num // 10
        num2 = num % 10
        
        num = num1 + num2 
        
        if num < 10:
            print(num)
            break
        
    else:
        print(0)
    
add_digit()