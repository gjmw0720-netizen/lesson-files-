numbers = [1, 2, 3, 4, 5, 6, 7]

result = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))

print(result)

# 出力: [1, 4, 3, 8, 5, 12, 7]