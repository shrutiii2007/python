def char_fre(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq   

s = "darshil"
print(char_fre(s))

# output:-
# {'d': 1, 'a': 1, 'r': 1, 's': 1, 'h': 1, 'i': 1, 'l': 1}