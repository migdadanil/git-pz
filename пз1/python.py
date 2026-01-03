#1
def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(climb_stairs(5))

#2
def max_subarray_sum(arr):
    if not arr:
        return 0
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)
    return max_global


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Максимальная сумма подотрезка:", max_subarray_sum(nums))

#3
def min_coins(n):
    coins = [1, 3, 4]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n]


print("Минимум монет для суммы 6:", min_coins(6))


#4
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,     # удаление
                dp[i][j - 1] + 1,     # вставка
                dp[i - 1][j - 1] + cost  # замена
            )
    return dp[m][n]


print("Расстояние Левенштейна между 'kitten' и 'sitting':", levenshtein_distance("kitten", "sitting"))





