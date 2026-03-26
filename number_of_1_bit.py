def number_of_1_bit(n:int)-> int:
    divisor = ''
    
    while n != 0:
        divisor += str(n % 2)
        n = n // 2
        
    return sum([int(i) for i in divisor])

print(number_of_1_bit(int(input("Numbers: "))))