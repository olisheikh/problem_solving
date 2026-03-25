def find_index():
    haystack = "a"
    needle = "a"
    
    needle_len = len(needle)
    
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            aa = len(haystack[i:])
            if len(haystack[i:]) >= needle_len:
                if haystack[i:i + needle_len] == needle:
                    return i 
                
    return -1

print(find_index())