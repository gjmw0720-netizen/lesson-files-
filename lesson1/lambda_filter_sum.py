# lambda_filter_sum.py

numbers = [12, 7, 5, 18, 21, 9, 10, 14, 3]

filtered = list(filter(lambda x: x % 3 == 0, numbers))

total = sum(filtered)

print("3の倍数の合計:", total)
