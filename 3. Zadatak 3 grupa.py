def najduzi_testerasti_podniz(arr):
    if len(arr) < 2:
        return []

    max_length = 0
    max_subsequence = []
    current_subsequence = [arr[0]]

    for i in range(1, len(arr)):
        if (len(current_subsequence) % 2 == 0 and arr[i] > current_subsequence[-1]) or \
           (len(current_subsequence) % 2 == 1 and arr[i] < current_subsequence[-1]):
            current_subsequence.append(arr[i])
        else:
            if len(current_subsequence) > max_length:
                max_length = len(current_subsequence)
                max_subsequence = current_subsequence
            current_subsequence = [arr[i]]

    if len(current_subsequence) > max_length:
        max_subsequence = current_subsequence

    return max_subsequence

arr = [1, 3, 2, 4, 3, 5, 4, 6]
testerasti_podniz = najduzi_testerasti_podniz(arr)
print("Najduži testerasti podniz:", testerasti_podniz)