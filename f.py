f = open(r'C:\Users\Наталья\Desktop\26-53.txt')
n = int(f.readline())
b = []

for i in range(0, n):
    b.append(int(f.readline()))

k = 0
m = -10 ** 10

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if b[i] % 2 != 0 and b[j] % 2 != 0 and (b[i] + b[j]) // 2 in b:
            k += 1
            m = max(m, (b[i] + b[j]) // 2)

print(k, m)
