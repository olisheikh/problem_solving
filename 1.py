order = [3,1,2,5,4] 
friends = [1,3,4]

finish_order = []

for i in order:
    if i in friends:
        finish_order.append(i)
        
print(finish_order)