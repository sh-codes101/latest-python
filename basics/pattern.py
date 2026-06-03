def patt(n):
    if n == 0:
        print('')
        return
    print('*'*n)
    patt(n-1)

n = int(input("no. : "))
patt(n) #recursion basicsss