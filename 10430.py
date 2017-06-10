a, b, c = input().split()
a, b, c = [int(i) for i in [a, b, c]]
print( (a+b)%c )
print( (a%c + b%c)%c )
print( (a*b)%c )
print( (a%c * b%c)%c )