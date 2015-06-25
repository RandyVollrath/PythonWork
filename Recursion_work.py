## Randy Vollrath

## Answer 1

## Recursive function that takes an arbitrarily nested list containing
## numbers and returns the maximum item in that list.
def maximum(numLst):
    
    if type(numLst)!=list:
        return numLst
    
    lst=[]

    for num in numLst:
        lst.append(maximum(num))
        
    return max(lst)

## Answer 2

## Recursive function that prints a stack of cups with a given number of 
## rows. 

def printstack(n,indentation=0):
    if n>0:
        printstack(n-1,indentation+1)
        print(indentation*" " + "U "*n)
        
        
if __name__ == '__main__':
    import doctest
    print(doctest.testfile('lab9TEST.py'))
