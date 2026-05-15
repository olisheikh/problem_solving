def fiz_buzz(n)-> List[str]:
    # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    # answer[i] == "Fizz" if i is divisible by 3.
    # answer[i] == "Buzz" if i is divisible by 5.
    # answer[i] == i (as a string) if none of the above conditions are true.
    
    final_ar = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            final_ar.append("FizzBuzz")
        elif i % 3 == 0:
            final_ar.append("Fizz")
        elif i % 5 == 0:
            final_ar.append("Buzz")
        else:
            final_ar.append(str(i))
            
    return final_ar

print(fiz_buzz(int(input("Enter number: "))))

