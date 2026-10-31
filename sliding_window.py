# for setting lowest neg value 

max_sum = float('-inf')

# for adding a char in dictoionary 

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1  # increase
for ch in t:
    freq[ch] = freq.get(ch, 0) - 1  # decrease



