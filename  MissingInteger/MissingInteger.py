# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    #convert array into set
    numbers = set(A)

    #Start checking from the smallest positive integer 
    missing = 1

    #keep checking while the number exists in the set 
    while missing in numbers: 
        missing += 1

    #return the smallest missing positive integer
    return missing 
    