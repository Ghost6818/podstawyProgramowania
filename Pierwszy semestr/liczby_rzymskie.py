symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
pairs = {}
for s, n in zip(symbols, numbers):
    pairs[s] = n

q = int(input())
while q > 0:
    a = input().split()
    results = []
    for i in range(len(a)):
        separated = [pairs[x] for x in a[i]]
        separated.reverse()
        j = len(separated)
        k = 0
        while j-1 > 0:
            if separated[k] > separated[k+1]:
                separated[k] -= separated[k+1]
                separated.remove(separated[k+1])
                j -= 2
            else:
                j -= 1
            k += 1
        results.append(sum(separated))
    # print(f"{results[0]} + {results[1]} = {sum(results)}")
    result = sum(results)
    result_ar = []
    while result > 0:
        for i in range(len(numbers)-1, -1, -1):
            if result - numbers[i] >= 0:
                result_ar.append(symbols[i])
                result -= numbers[i]
                break
    print("".join(result_ar))
    q -= 1