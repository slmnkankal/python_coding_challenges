n = int(input("Enter a positive number: "))
prime_list = []
for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        prime_list.append(num)
print(prime_list)