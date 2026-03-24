n=5
s= 'ab'
def count_string(n,s):
    k=len(s)
    count=0
    for i in range (n-k+1):
        count+= 4**(n-k)
    return count
print(count_string(n,s))