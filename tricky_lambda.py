def my_multix():
    return [lambda x: x*n for n in range(4)]
    
print [m(2) for m in my_multix()]

# output = [6, 6, 6, 6]
