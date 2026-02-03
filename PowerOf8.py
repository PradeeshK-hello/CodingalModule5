def powerOf8(n):
    if n <= 0:
        return False
    x = round(n ** (1/8))
    return x ** 8 == n
n = int(input("Enter your number: "))
if powerOf8(n):
    print(f"{n} is a power of 8.")
else:
    print(f"{n} is not a power of 8.")