def canReach(ar, s):
    if ar[s] == 0:
        return True
    temp = s
    for i in range(len(ar)):
        if temp < len(ar):
            addition = temp + ar[temp]
            subtraction = temp - ar[temp]
            
        if ar[addition] == 0 or ar[subtraction]:
            return True
        
        temp = 


arr = [4,2,3,0,3,1,2]
start = 5

print(canReach(arr, start))