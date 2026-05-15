def strictly_palindromic_number(num)-> bool:
    for i in range(2, num -1):
        base = ''
        rem = num
        while rem != 0:
            base += str(rem % i)
            rem = rem // i 
            
        str_rem = "" + ''.join(reversed(base))
        reverse_rem = ''.join(reversed(str_rem))
        
        if str_rem != reverse_rem:
            return False
        
    return True 


num = int(input("Enter the number: "))
print(strictly_palindromic_number(num))