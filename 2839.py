n = int( input() )

# 5kg bag
b = n//5
r = n%5

# 3kg bag
s = r//3
r = r%3

if r==2 and s>0:
    b+=1
    s-=1
elif r==2:
    b-=2
    s+=4
elif r==1:
    b-=1
    s+=2

if b<0 or s<0:
    print(-1)
else:
    print(b+s)