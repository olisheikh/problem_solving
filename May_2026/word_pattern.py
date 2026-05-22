
pattern = "abba"
s = "dog cat ca dog"

p_list = [i for i in pattern]
s_list = s.split(' ')

ps = [p + s for p, s in zip(p_list, s_list)]


for i in range(len(pattern)):
    if pattern.count(pattern[i]) != ps.count(ps[i]):
        print(False)
        
print(True)