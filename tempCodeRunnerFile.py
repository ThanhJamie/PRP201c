def getint(message, min):
    while True:
        try:
            a = int(input(message))
            if a >= min:
                return a
            else:
                print("The number must be positive.")
        except Exception:
            print("The number must be a positive number.")


num = getint("Enter a positive integer number: ", 0)
print("The prime numbers from 0 to "+str(num)+" :" )

for i in range(0,num+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
