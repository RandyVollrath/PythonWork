def fib(n):    
    # calculates the fibonacci number at a specified index
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def fibLst(endNum):
    #returns fibonaci sequence up to specified number of numbers 
    lst = []
    for i in range(0,endNum):
        lst.append(fib(i))
    return lst

def addEvens(endNum):
    # adds all even numbers in fib sequence up to specified index
    evenLst = []
    for nums in fibLst(endNum):
        if nums % 2 == 0:
            evenLst.append(nums)

    a = 0
    for nums in evenLst:
        a+=nums
    return a
