s = "abc"
t = "ahbgdc"

count_s = 0

for i in s:
    if i in t:
        count_s += 1
        
if count_s == len(s):
    print(True)
else:
    print(False)