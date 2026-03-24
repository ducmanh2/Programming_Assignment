#problem 1
#1
def Next(s):
    if s == "":
        return "a"
    last_char = s[-1]
    if last_char == 'd':
        return Next(s[:-1]) + 'a'
    else:
        return s[:-1] + chr(ord(last_char) + 1)
#2
def previous_palindrome(s):
    A=['a','b','c','d']
    n=len(s)
    def make_pal(left):
        if n%2 == 0:
            return left+left[::-1]
        else:
            return left+left[:-1][::-1]
    def decrease(left):
        left = list(left)
        i = len(left) - 1
        while i >= 0:
            if left[i] != 'a':
                left[i] = A[A.index(left[i]) - 1]
                break
            else:
                left[i] = 'd'
                i -= 1
        if i < 0:
            return None

        return ''.join(left)

    half_len = (n + 1) // 2
    left = s[:half_len]

    pal = make_pal(left)

    if pal < s:
        return pal
    new_left = decrease(left)

    if new_left is None:
        return "d" * (n-1)

    return make_pal(new_left)



#problem 2
#1
def product(M,N):
    mult_res=[[0,0],[0,0]]
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                mult_res[i][j] +=M[i][k] * N[k][j]
    print('product of 2 matrices M and N is: ')
    for result in mult_res:
        print(result)




def main():
    test_cases1 = ['abcd','ddabda']

    for t in test_cases1:
        result = previous_palindrome(t)
        print(f'Next({t}) = {Next(t)}')
        print(f'The previous palindrome of {t} is {result}')
    M=[[1,2],[3,4]]
    N=[[4,3],[2,1]]
    print(f'Product of 2 matrices M and N is: {product(M,N)}')


if __name__ == "__main__":
    main()