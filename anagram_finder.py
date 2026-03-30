def anagram():
    s = "anagram"
    t = "nagaram"
    is_anagram = True
        
    if len(s) != len(t):
        is_anagram = False
    else:
        for i in s:
            if i not in t:
                is_anagram = False
                break
            else:
                t = t.replace(i, '')
    
    print(is_anagram)
    
anagram()