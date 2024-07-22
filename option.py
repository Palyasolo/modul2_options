N = int(input("Введите число от 3 до 23 "))
if N < 3 or N > 23:
    N = int(input("Неверное число. Введите число от 3 до 23 "))
print (N)

numbers = []
for i in range (N):
    numbers.append (i+1)
#print (numbers)

primes = []
for i in numbers[1:]:
    if N % i == 0:
        primes.append (i)
    continue
#print (primes)

results = []
b = 1
for i in primes:
    a = i // 2
    b = 1
    for j in range (a):
        results.append (b)
        c = i - b
        results.append(c)
        b += 1
results_2 = int(''.join(map(str, results)))
print (results_2)