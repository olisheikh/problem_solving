s = "abcabcbb"

long_list = []
count = 0
re_s = s[0]

for i in s[1:]:
    if i not in re_s:
        re_s += i
        count += 1
    else:
        re_s = i
        long_list.append(count)
        count = 0
        
print(max(long_list) + 1)