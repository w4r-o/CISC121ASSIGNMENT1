# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    #Get length of array
    length = len(A) 

    #if array empty return it
    if length == 0:
        return A
    
    #avoid unnecessary rotations
    K = K % length

    #rotate the array K times
    for i in range(K):
        #get the last element
        last = A[-1]
        #remove last element
        A.pop()
        #insert at beginning
        A.insert(0,last)
    
    return A
    

 