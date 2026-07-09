queries = [3,1,2,1] 
m = 5


demo_list = []
result_list = []

for i in range(1, m + 1):
    demo_list.append(i)
    
for i in range(len(queries)):
    result_list.append(demo_list.index(queries[i]))
    demo_list.remove(queries[i])
    demo_list.insert(0, queries[i])
    
print(result_list)
    
    