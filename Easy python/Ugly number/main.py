def ugly_number(n):
    ugly_numbers = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly_numbers) < n:
        next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
        ugly_numbers.append(next_ugly)

        if next_ugly == ugly_numbers[i2] * 2:
            i2 += 1
        if next_ugly == ugly_numbers[i3] * 3:
            i3 += 1
        if next_ugly == ugly_numbers[i5] * 5:
            i5 += 1
    return ugly_numbers[-1]


# Masalani tekshirish
n = 10
result = ugly_number(n)
print(f"{n}-ta ugly number: {result}")

# Chat GPT