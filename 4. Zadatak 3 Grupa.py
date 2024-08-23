def count_adjacent_matches(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count

# Primjer
s = "aabaaac"
rezultat = count_adjacent_matches(s)
print(rezultat)
