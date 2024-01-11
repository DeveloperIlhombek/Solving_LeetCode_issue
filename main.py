def sumOddLengthSubarrays(arr):
    length = len(arr)
    result = 0

    for start in range(length):
        for end in range(start, length, 2):
            result += sum(arr[start:end + 1])
    return result

# Example usage:
arr = [1, 4, 2, 5, 3]
result = sumOddLengthSubarrays(arr)
print(result)
