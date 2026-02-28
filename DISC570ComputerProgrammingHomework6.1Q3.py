def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return print(x)

while True:
    try:
        n = int(input("Enter a whole number to factorize: "))
        break
    except ValueError:
        print("Not valid, please enter a whole number.")

if n < 0:
    print("Can't factorize a negative number.")
else:
    factorial(n)