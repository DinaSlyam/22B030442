

def all(n):
    while n>=0:
        yield n
        n-=1
for i in all(10):
    print(i)
