def reverse_last_digit(n,r):
    if n <= 9:
        return (r*10 + n)
    else:
        return reverse_last_digit((n - n % 10) / 10, r*10+(n%10))


def reverse_number(n):
    sign = 1 if n > 0 else -1
    return reverse_last_digit(abs(n),0) * sign

