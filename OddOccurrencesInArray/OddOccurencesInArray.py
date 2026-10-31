# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    result = 0

    #go thru every number in the array
    for num in A:
        #xor each number w the result
        result ^= num 
    
    return result

