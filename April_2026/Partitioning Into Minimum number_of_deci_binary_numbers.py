boxes = "001011"
final_list = []
count_element = 0

for i in range(len(boxes)):
    summation = 0
    for j in range(len(boxes)):
        if boxes[j] == '1':
            summation += abs(j - i)
            
    final_list.append(summation)
    
print(final_list)
            