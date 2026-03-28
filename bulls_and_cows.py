def bulls_and_cows(self, secret: str, guess: str) -> str:
    bulls = 0
    bulls_list = []
    cows = 0
    cows_list = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        else:
            bulls_list.append(secret[i])
            cows_list.append(guess[i])

    length = len(bulls_list)    

    for i in range(length):
        if cows_list[i] in bulls_list:
            bulls_list.remove(cows_list[i])
            cows += 1
    
    print(f'{bulls}A{cows}B')
    
bulls_and_cows()