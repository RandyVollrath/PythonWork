# Name: Randy Vollrath

#Answer 1

# Recursive function that generates a specific pattern. First argument
# is always a power of 2 and is the max number of stars appearing in
# the middle row. The second argument (which defaults to 0) is the
# number of spaces to put before each patterns rows of stars

def printPattern(n,shift=0):
    'prints * patterns'
    if n>0:
        printPattern(n//2,shift) #shift by n//2
        print(shift*' '+n*'*')
        printPattern(n//2,shift+n//2)

## returns the greatest common divisor of a pair of numbers. The gcd of m and n
## is the largest number that divides both m and n. 

def gcd(m,n): # simply saying if n exist, then run: prev,curr = curr,prev%curr
    'finds the greatest common divisor between 2 numbers'
    while n:
        m , n = n, m%n
    return m
        

# Recursive function that finds the number of occurences of target in a nested
# list, where each item in the list is either a number or another list. 

def flatten( tree ):
        if type(tree)!=list:
            return[tree]
        else:
            ans = []
            for branch in tree:
                ans += ( flatten(branch) )
                # or, ans.extend(flatten(branch))
            return (ans)

def count(lst,target):
    'will call flatten to generate 1 list, and count the number of time it matches the target'
    newlst = []
    newlst = flatten(lst)
    return(newlst.count(target))

if __name__ == '__main__':
    import doctest
    print(doctest.testfile('lab7TEST.py'))


