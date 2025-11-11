def is_prime(number):
    if number>1:
        for number in range (2,number):
            if number%num==0:
                return "not a prime"
            return "prime"
        return "not a prime"
    print(is_prime(5))