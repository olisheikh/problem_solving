s = "babad"
s_rev = s[::-1]
p_s = s[0]
f_s = ""
for i in range(1, len(s)):
    p_s += s[i]
    if p_s == p_s[::-1]:
        f_s = p_s
    else:
        p_s = p_s[i:]
        
        
print(f_s)

