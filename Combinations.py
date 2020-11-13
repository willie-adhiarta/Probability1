import math
# Combinations Code
n = 52
k = 2

# Determine Permutaions
Permutations = math.factorial(n) / math.factorial(n - k)

# Determine Combinations and print result
Combinations = Permutations / math.factorial(k)
print(Combinations)