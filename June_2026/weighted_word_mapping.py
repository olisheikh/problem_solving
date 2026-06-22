alp = [
    "z",
    "y",
    "x",
    "w",
    "v",
    "u",
    "t",
    "s",
    "r",
    "q",
    "p",
    "o",
    "n",
    "m",
    "l",
    "k",
    "j",
    "i",
    "h",
    "g",
    "f",
    "e",
    "d",
    "c",
    "b",
    "a",
]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

str = ["abcd","def","xyz"]
join_str = ''.join(str)
sum = 0
count = 0
new_str = ''
for i in range(len(join_str)):
    print(str[count])
    if i < len(str[count]):
        sum += weights[i]
        
    else:
        count += 1
        sum = 0
        index_value = sum % 26
        new_str += alp[index_value]
        
print(new_str)

